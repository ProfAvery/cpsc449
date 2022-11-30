# See https://docs.github.com/en/developers/webhooks-and-events/webhooks/configuring-your-server-to-receive-payloads

import json
from quart import Quart, request

app = Quart(__name__)


@app.route("/payload", methods=["POST"])
async def inspect_push():
    push = await request.get_json()
    app.logger.debug(json.dumps(push, indent=2))
    return "", 204
