# Code by ByungWook.Kang @lesimor
from slacker import Slacker
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from bots.examples.hello import HelloBot

hello_bot = HelloBot()


@require_http_methods(["GET"])
def slack_herbot(request):
    token = 'xoxb-673155478773-661863038434-bVqaHtcT4fcNdjGj18kgz21C'
    slack = Slacker(token)

    qd = request.GET
    params = qd.dict()

    slack.chat.post_message('#{}'.format(params.get('channel', '')), params.get('message', ''))

    return JsonResponse({
        'status': 'ok'
    }, json_dumps_params={'ensure_ascii': True})


@require_http_methods(["POST"])
def slack_outgoing_webhook(request):
    channel = request.POST.get('channel_name')
    username = request.POST.get('user_name')
    text = request.POST.get('text')

    return JsonResponse({
        "text": hello_bot.response(text)
    }, json_dumps_params={'ensure_ascii': True})
