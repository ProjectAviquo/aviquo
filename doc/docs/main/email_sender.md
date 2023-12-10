# email_sender.py

## Overview

Create and send emails, like the password reset.

## Module Objects

### Email

:   The main email class

#### __init__()

:   Create an email with a context, reciever, and sender info.

#### createHeaders()

:   Adds requried email headers:

    * Subject
    * From
    * To

#### createBody()

:   Set the HTML body of the email to the provided.

#### sendMessage()

:   Nyomm

:   Sends through gmail SMTP

### EmailPasswordResetForm

:   Form for the password reset email

#### send_mail()

:   Sends an [Email](#email) with the password reset form, with the [CustomPasswordResetView](#custompasswordresetview) view

### CustomPasswordResetView

:   View for the reset form, using form [EmailPasswordResetForm](#emailpasswordresetform)
