from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import user_messages


@login_required
def messages_page(request):

    selected_message = None
    mode = "new"

    # -----------------------
    # GET USER DATA FIRST
    # -----------------------
    inbox = user_messages.objects.filter(receiver=request.user, is_draft=False)
    sent = user_messages.objects.filter(sender=request.user, is_draft=False)
    drafts = user_messages.objects.filter(sender=request.user, is_draft=True)

    # -----------------------
    # HANDLE CLICKED MESSAGE
    # -----------------------
    message_id = request.GET.get('message_id')

    if message_id:
        selected_message = get_object_or_404(user_messages, id=message_id)

        # SECURITY (you were missing this)
        if selected_message.sender != request.user and selected_message.receiver != request.user:
            selected_message = None
        else:
            if selected_message.is_draft:
                mode = "edit"
            else:
                mode = "view"

    # -----------------------
    # HANDLE FORM SUBMIT
    # -----------------------
    if request.method == 'POST':

        draft_id = request.POST.get("draft_id")
        action = request.POST.get('action')
        receiver_email = request.POST.get('receiver_email')
        subject = request.POST.get('subject')
        body = request.POST.get('body')

        receiver = User.objects.filter(email=receiver_email).first()

        draft_id = request.POST.get('draft_id')

        # DELETE DRAFT
        if action == "delete" and draft_id:
            draft = user_messages.objects.filter(
                id=draft_id,
                sender=request.user,
                is_draft=True
            ).first()

            if draft:
                draft.delete()

            return redirect('/messages/')

        # -----------------------
        # SEND VALIDATION
        # -----------------------
        if action == "send":
            if not receiver_email or not receiver or not subject:
                return redirect('/messages/')

        # -----------------------
        # DRAFT VALIDATION
        # -----------------------
        if action == "draft":
            if not receiver_email and not subject and not body:
                # ALL EMPTY → block
                return redirect('/messages/')

        if draft_id:
            # UPDATE existing draft
            draft = get_object_or_404(user_messages, id=draft_id, sender=request.user)

            draft.receiver = receiver
            draft.subject = subject
            draft.body = body
            draft.is_draft = (action == "draft")

            draft.save()
        else:
            # CREATE new message
            user_messages.objects.create(
                sender=request.user,
                receiver=receiver,
                subject=subject,
                body=body,
                is_draft=(action == 'draft')
            )

        return redirect('/messages/')

    return render(request, 'MessagePage.html', {
        'inbox': inbox,
        'sent': sent,
        'drafts': drafts,
        'selected_message': selected_message,
        'mode': mode,
        'inbox_empty': not inbox.exists()  # 👈 pass to template
    })