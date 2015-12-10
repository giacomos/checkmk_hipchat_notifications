#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

register_notification_parameters("hipchat",
    Dictionary(
        elements=[
            (
                "token",
                TextAscii(
                    title=_("Token"),
                    help=_('HipChat API token to use'),
                    size=40,
                    allow_empty=False,
                )
            ),
            (
                "room_id",
                TextAscii(
                    title=_("Room ID"),
                    help=_('HipChat room id deliver message to'),
                    size=40,
                    allow_empty=False,
                )
            ),
            (
                "api_version",
                DropdownChoice(
                    title = _("Api Version"),
                    choices = [
                        ( "2", _("2") ),
                        ("1", _("1") )],
                    default_value=2
                )
            ),
            (
                "api_host",
                TextAscii(
                    title=_("Api Host"),
                    help=_('HipChat Server to deliver message to (default:api.hipchat.com)'),
                    size=40,
                    allow_empty=False,
                    default_value="api.hipchat.com"
                )
            ),
            (
                "user",
                TextAscii(
                    title=_("User"),
                    help=_('Username to deliver message as, when using API version 1'),
                    size=40,
                    allow_empty=False,
                )
            ),
            (
                "msg_format",
                DropdownChoice(
                    title=_("Message Format"),
                    help=_('Determines how messages are rendered by HipChat.Valid values: html, text. Defaults to html.'),
                    choices=[
                        ("html", _("html")),
                        ("text", _("text")),
                    ],
                )
            ),
            (
                "proxy",
                TextAscii(
                    title=_("Proxy"),
                    help=_('Specify a proxy in the form [user:passwd@]proxy.server:port.'),
                    size=40,
                    allow_empty=False,
                )
            ),
            (
                "msg_type",
                DropdownChoice(
                    title=_("Message Type"),
                    help=_('Mark if notification is from host group or service group, host|service|short-host|short-service'),
                    choices=[
                        ("host", _("host")),
                        ("short-host", _("short-host")),
                        ("service", _("service")),
                        ("short-service", _("short-service")),
                    ],
                )
            ),
        ]
    )
)
