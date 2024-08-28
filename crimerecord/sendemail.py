import sib_api_v3_sdk
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
from .models import *

def sendmail(sender, toemail, toname, fromemail, subject, pid, request):
    fir = Fir.objects.get(id=pid)
    userid = User.objects.get(id=request.user.id)
    policeid = Police.objects.get(user=userid)
    newfir = Fir.objects.filter(policestationid=policeid.policestationid, status=None)
    newfircount = Fir.objects.filter(policestationid=policeid.policestationid, status=None).count()
    html_message = render_to_string('fir_details_email.html', locals())
    plain_message = strip_tags(html_message)

    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = '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'
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    subject = subject
    html_content = html_message
    sender = {"name": sender, "email": fromemail}
    to = [{"email": toemail, "name": toname}]
    headers = {"Some-Custom-Name": "unique-id-1234"}
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, headers=headers,html_content=html_content, sender=sender, subject=subject)
    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
