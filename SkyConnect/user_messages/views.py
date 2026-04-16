from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import user_messages


@login_required
def messages_page(request):

    selected_message = None
    mode = "new"  # new, view, edit

    # HANDLE CLICKED MESSAGE
    message_id = request.GET.get('message_id')

    if message_id:
        selected_message = get_object_or_404(user_messages, id=message_id)

        if selected_message.is_draft:
            mode = "edit"
        else:
            mode = "view"

    # HANDLE FORM SUBMIT
    if request.method == 'POST':
        action = request.POST.get('action')

        receiver_email = request.POST.get('receiver_email')
        subject = request.POST.get('subject')
        body = request.POST.get('body')

        receiver = None

        if receiver_email:
            try:
                receiver = User.objects.get(email=receiver_email)
            except User.DoesNotExist:
                receiver = None

        user_messages.objects.create(
            sender=request.user,
            receiver=receiver,
            subject=subject,
            body=body,
            is_draft=(action == 'draft')
        )

        return redirect('/messages/')

    inbox = user_messages.objects.filter(receiver=request.user, is_draft=False)
    sent = user_messages.objects.filter(sender=request.user, is_draft=False)
    drafts = user_messages.objects.filter(sender=request.user, is_draft=True)

    return render(request, 'MessagePage.html', {
        'inbox': inbox,
        'sent': sent,
        'drafts': drafts,
        'selected_message': selected_message,
        'mode': mode
    })