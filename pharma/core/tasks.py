
from core.models import drugs,result
import twilio.rest
from celery import shared_task
from django.core.mail import send_mail
from pharma import settings
from datetime import date,timedelta
from django.core.mail import EmailMultiAlternatives

@shared_task(bind=True)
def send_mail_func(self):
    # Get all instances of the result model
    all_results = result.objects.all()

    for res in all_results:
        # Calculate alert dates for 3, 6, 9, and 12 months
        alert_date = res.alert_date 
        alert_3_months = alert_date + timedelta(days=1)  # Assuming 30 days per month
        alert_6_months = alert_date + timedelta(days=0)
        alert_9_months = alert_date + timedelta(days=270)
        alert_12_months = alert_date +timedelta(days=365)

        current_date = date.today()

        alerts = []
        if current_date == alert_3_months:
            alerts.append(3)
        if current_date == alert_6_months:
            alerts.append(6)
        if current_date == alert_9_months :
            alerts.append(9)
        if current_date == alert_12_months :
            alerts.append(12)

        # If there are alerts, send emails
        for alert_interval in alerts:
            user_email = res.drug.email  # Assuming a OneToOneField to drugs
            mail_subject = f"Alert for {alert_interval}-month {res.stability} stability "
            message = f"""
            <h1>Dear {res.drug.Name},</h1>
            <h2>Alert for {alert_interval}-month stability alert</h2>
            <table border="1">
              <tr>
                <th>Product Name</th>
                <th>Batch No.</th>
                <th>Mfg Date</th>
                <th>Stability</th>
                <!-- Add more columns as needed -->
              </tr>
              <tr>
                <td>{res.drug.Productname}</td>
                <td>{res.drug.batch}</td>
                <td>{res.drug.mfg}</td>
                <td>{res.stability}</td>
                <!-- Add more cells as needed -->
              </tr>
            </table>
            """
            
            msg = EmailMultiAlternatives(
                subject=mail_subject,
                from_email=settings.EMAIL_HOST_USER,
                to=[user_email],
            )
            msg.attach_alternative(message, "text/html")
            msg.send(fail_silently=True)
    return "done"


@shared_task(bind=True)
def send_sms(self):
    account_sid = "AC3accb0615c53343f9564326db68f9c0d"
    auth_token = "49d8a46bc6ea246c9044eb2b2edc8caa"

    # Create a Twilio client
    client = twilio.rest.Client(account_sid, auth_token)

    # Get all instances of the result model
    all_results = result.objects.all()

    for res in all_results:
        # Calculate alert dates for 3, 6, 9, and 12 months
        alert_date = res.alert_date
        alert_3_months = alert_date + timedelta(days=1)  # Assuming 30 days per month
        alert_6_months = alert_date + timedelta(days=180)
        alert_9_months = alert_date + timedelta(days=270)
        alert_12_months = alert_date + timedelta(days=365)

        current_date = date.today()

        alerts = []
        if current_date == alert_3_months:
            alerts.append(3)
        if current_date == alert_6_months:
            alerts.append(6)
        if current_date == alert_9_months:
            alerts.append(9)
        if current_date == alert_12_months:
            alerts.append(12)

        # If there are alerts, send SMS
        for alert_interval in alerts:
            user_phone_number = res.drug.mobile  # Replace with the actual field
            body = f"Alert for {alert_interval}-month stability: {res.drug.Productname}"
            
            message = client.messages.create(
                to="+91"+str(user_phone_number),
                from_="+14844942570",
                body=body
            )

    return "done"




'''


            mail_subject = f"Alert for {alert_interval}-month stability"
            to_email = user_email

            send_mail(
                subject=mail_subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[to_email],
                fail_silently=True,
            )
def send_mail_func(self):
    #operation
    all_drugs= drugs.objects.all()
    users = [drug.email for drug in all_drugs]
    all_dates=result.objects.all()
    dates=[result.alert_date for da in all_dates]
    current_date = date.today()

    for d in dates:
        if d==current_date: 
            for user in users:
                mail_subject ="hey testing in going on of perodic task"
                message="working"
                to_email = user

                send_mail(
                    subject=mail_subject,
                    message=message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[to_email],
                    fail_silently=True,
                    
                )
    
    return "done"
    ---------------

    @shared_task(bind=True)
def send_mail_func(self):
    # Operation
    current_date = date.today()
    #all_drugs = result.objects.select_related('drug').all()
   # users = [drug.email for drug in all_drugs]

    all_results = result.objects.select_related('drug').all()

    for res in all_results:
        alert_date = res.alert_date

        # Compare year, month, and day separately
        if alert_date.year == current_date.year and alert_date.month == current_date.month and alert_date.day == current_date.day:
            user_email = res.drug.email
            mail_subject = "Hey, working"
            message = "passed"
            to_email = user_email

            send_mail(
                    subject=mail_subject,
                    message=message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[to_email],
                    fail_silently=True,
                )

    return "done"

    --------------------------------

    @shared_task(bind=True)
def send_sms(self):
    account_sid = "AC3accb0615c53343f9564326db68f9c0d"
    auth_token = "49d8a46bc6ea246c9044eb2b2edc8caa"

    # Create a Twilio client
    client = twilio.rest.Client(account_sid, auth_token)
    message = client.messages.create(
    to="+919106361197",
    from_="+14844942570",
    body="new perodic task"
    )

    return "done"


'''