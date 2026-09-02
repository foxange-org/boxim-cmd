#https://github.com/foxange-org/boxim-cmd
#制作者 : SLC_Extreme
import os
import sys
import time
import getpass

YELLOW = "\033[33m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RED = "\033[31m"
END = "\033[0m"

LANG = "en"

I18N = {
    "zh": {
        "err_no_sdk": "未检测到 boxim Python sdk，正在下载...",
        "update_pip": "更新 pip",
        "download_sdk": "下载 boxim-sdk",
        "user_name_label": "用户名:",
        "user_password_label": "密码:",
        "login_to_boxim": "正在登录 boxim",
        "input_user_name": "请输入用户名: ",
        "input_user_password": "请输入密码: ",
        "login_doing": "登录中...",
        "sign_to_boxim": "正在注册 boxim 账号",
        "sign_doing": "注册中...",
        "sign_success": "注册成功",
        "login_success": "登录成功",
        "auto_login_success": "已自动登录",
        "err_exit_int": "退出码必须是整数类型",
        "no_friends": "没有好友",
        "friends_and_ids": "好友及 ID:",
        "id_label": "ID",
        "name_label": "名称",
        "no_groups": "没有群组",
        "groups_and_ids": "群组及 ID:",
        "group_members": "群 {group_id} 的成员:",
        "no_members": "没有成员",
        "err_unknown_command": "未知命令: {list_token}",
        "recent_messages_with": "与 {friend_id} 的最近消息:",
        "no_messages": "未找到消息。",
        "recent_group_messages_in": "群 {group_id} 的最近消息:",
        "no_group_messages": "未找到群消息。",
        "unread_private_messages": "未读私聊消息:",
        "no_unread_messages": "没有未读消息",
        "err_msg_empty": "消息内容为空",
        "message_sent_to": "消息已发送给 {friend_id}。",
        "group_message_sent_to": "群消息已发送到 {group_id}。",
        "friend_request_sent_to": "好友请求已发送给 {user_id}。",
        "err_need_user_id": "至少需要一个用户 ID",
        "invited_to_group": "已邀请 {user_ids} 加入群 {group_id}。",
        "err_unknown_add_target": "未知的 add 目标: {sub}",
        "friend_deleted": "好友 {user_id} 已删除。",
        "removed_from_group": "已将 {user_ids} 移出群 {group_id}。",
        "err_unknown_del_target": "未知的 del 目标: {sub}",
        "err_group_name_empty": "群名称为空",
        "group_created": "群组已创建: id={group_id} name={group_name}",
        "err_unknown_new_target": "未知的 new 目标: {sub}",
        "group_deleted": "群 {group_id} 已删除。",
        "user_muted_in_group": "用户 {user_id} 已在群 {group_id} 中被禁言。",
        "user_unmuted_in_group": "用户 {user_id} 已在群 {group_id} 中解除禁言。",
        "group_flag_set": "群 {group_id} 的 {sub} 已设置为 {flag}。",
        "err_name_empty": "名称为空",
        "group_name_updated": "群 {group_id} 名称已更新。",
        "group_notice_updated": "群 {group_id} 公告已更新。",
        "err_unknown_set_option": "未知的 set 选项: {sub}",
        "err_unknown_mygroup_action": "未知的 mygroup 操作: {action}",
        "err_remark_empty": "备注内容为空",
        "group_remark_updated": "群 {group_id} 备注已更新。",
        "err_unknown_groups_set_option": "未知的 groups set 选项: {option}",
        "err_unknown_groups_action": "未知的 groups 操作: {sub}",
        "err_user_not_found": "用户 {friend_id} 不存在",
        "user_card_sent_to_friend": "已将用户 {friend_id} 的名片发送给好友 {target_friend_id}。",
        "user_card_sent_to_group": "已将用户 {friend_id} 的名片发送到群 {group_id}。",
        "err_unknown_recommend_target": "未知的 recommend 目标: {target}",
        "help_available": "可用命令:",
        "help_whoami": "显示当前登录用户名和密码",
        "help_login": "登录账号，无参数则逐个输入",
        "help_sign": "注册账号，无参数则逐个输入",
        "help_exit": "退出程序",
        "help_list_friends": "列出好友",
        "help_list_groups": "列出群组",
        "help_get_history": "查看私聊历史消息",
        "help_get_ghistory": "查看群聊历史消息",
        "help_get_unread": "查看未读私聊消息",
        "help_send": "发送私聊消息",
        "help_gsend": "发送群消息",
        "help_add_friend": "发送好友请求",
        "help_add_group": "邀请用户加入群",
        "help_del_friend": "删除好友",
        "help_del_group": "将用户移出群",
        "help_new_group": "创建群组",
        "help_mygroup_del_this": "解散群",
        "help_mygroup_mute": "禁言用户",
        "help_mygroup_unmute": "解除禁言",
        "help_mygroup_set_flag": "设置群开关",
        "help_mygroup_set_name": "修改群名称",
        "help_mygroup_set_notice": "修改群公告",
        "help_groups_set": "设置群备注名",
        "help_groups_list": "显示群成员列表",
        "help_recommend_friend": "发送用户名片给好友",
        "help_recommend_group": "发送用户名片到群",
        "help_cls": "清屏",
        "unknown_time": "未知时间",
    },
    "en": {
        "err_no_sdk": "boxim Python sdk not found, downloading...",
        "update_pip": "update pip",
        "download_sdk": "download boxim-sdk",
        "user_name_label": "user name:",
        "user_password_label": "user password:",
        "login_to_boxim": "login to boxim",
        "input_user_name": "input user name: ",
        "input_user_password": "input user password: ",
        "login_doing": "login...",
        "sign_to_boxim": "sign up to boxim",
        "sign_doing": "sign up...",
        "sign_success": "sign up success",
        "login_success": "login success",
        "auto_login_success": "auto logged in",
        "err_exit_int": "exit value must be int type",
        "no_friends": "don't have friends",
        "friends_and_ids": "friends and ids:",
        "id_label": "ID",
        "name_label": "Name",
        "no_groups": "don't have groups",
        "groups_and_ids": "groups and ids:",
        "group_members": "members of group {group_id}:",
        "no_members": "no members",
        "err_unknown_command": "unknown command: {list_token}",
        "recent_messages_with": "Recent messages with {friend_id}:",
        "no_messages": "No messages found.",
        "recent_group_messages_in": "Recent group messages in {group_id}:",
        "no_group_messages": "No group messages found.",
        "unread_private_messages": "Unread private messages:",
        "no_unread_messages": "no unread messages",
        "err_msg_empty": "message text is empty",
        "message_sent_to": "Message sent to {friend_id}.",
        "group_message_sent_to": "Group message sent to {group_id}.",
        "friend_request_sent_to": "Friend request sent to {user_id}.",
        "err_need_user_id": "need at least one user id",
        "invited_to_group": "Invited {user_ids} to group {group_id}.",
        "err_unknown_add_target": "unknown add target: {sub}",
        "friend_deleted": "Friend {user_id} deleted.",
        "removed_from_group": "Removed {user_ids} from group {group_id}.",
        "err_unknown_del_target": "unknown del target: {sub}",
        "err_group_name_empty": "group name is empty",
        "group_created": "Group created: id={group_id} name={group_name}",
        "err_unknown_new_target": "unknown new target: {sub}",
        "group_deleted": "Group {group_id} deleted.",
        "user_muted_in_group": "User {user_id} muted in group {group_id}.",
        "user_unmuted_in_group": "User {user_id} unmuted in group {group_id}.",
        "group_flag_set": "Group {group_id} {sub} set to {flag}.",
        "err_name_empty": "name is empty",
        "group_name_updated": "Group {group_id} name updated.",
        "group_notice_updated": "Group {group_id} notice updated.",
        "err_unknown_set_option": "unknown set option: {sub}",
        "err_unknown_mygroup_action": "unknown mygroup action: {action}",
        "err_remark_empty": "remark text is empty",
        "group_remark_updated": "Group {group_id} remark updated.",
        "err_unknown_groups_set_option": "unknown groups set option: {option}",
        "err_unknown_groups_action": "unknown groups action: {sub}",
        "err_user_not_found": "user {friend_id} not found",
        "user_card_sent_to_friend": "User card of {friend_id} sent to friend {target_friend_id}.",
        "user_card_sent_to_group": "User card of {friend_id} sent to group {group_id}.",
        "err_unknown_recommend_target": "unknown recommend target: {target}",
        "help_available": "Available commands:",
        "help_whoami": "display current login username and password",
        "help_login": "login account, input one by one if no arguments",
        "help_sign": "register account, input one by one if no arguments",
        "help_exit": "exit program",
        "help_list_friends": "list friends",
        "help_list_groups": "list groups",
        "help_get_history": "view private chat history",
        "help_get_ghistory": "view group chat history",
        "help_get_unread": "view unread private messages",
        "help_send": "send private message",
        "help_gsend": "send group message",
        "help_add_friend": "send friend request",
        "help_add_group": "invite users to group",
        "help_del_friend": "delete friend",
        "help_del_group": "remove users from group",
        "help_new_group": "create group",
        "help_mygroup_del_this": "dismiss the group",
        "help_mygroup_mute": "mute user",
        "help_mygroup_unmute": "unmute user",
        "help_mygroup_set_flag": "set group switch",
        "help_mygroup_set_name": "modify group name",
        "help_mygroup_set_notice": "modify group notice",
        "help_groups_set": "set group remark name",
        "help_groups_list": "show group members",
        "help_recommend_friend": "send user card to friend",
        "help_recommend_group": "send user card to group",
        "help_cls": "clear screen",
        "unknown_time": "unknown time",
    },
    "tw": {
        "err_no_sdk": "未偵測到 boxim Python sdk，正在下載...",
        "update_pip": "更新 pip",
        "download_sdk": "下載 boxim-sdk",
        "user_name_label": "使用者名稱:",
        "user_password_label": "密碼:",
        "login_to_boxim": "正在登入 boxim",
        "input_user_name": "請輸入使用者名稱: ",
        "input_user_password": "請輸入密碼: ",
        "login_doing": "登入中...",
        "sign_to_boxim": "正在註冊 boxim 帳號",
        "sign_doing": "註冊中...",
        "sign_success": "註冊成功",
        "login_success": "登入成功",
        "auto_login_success": "已自動登入",
        "err_exit_int": "退出碼必須是整數型別",
        "no_friends": "沒有好友",
        "friends_and_ids": "好友及 ID:",
        "id_label": "ID",
        "name_label": "名稱",
        "no_groups": "沒有群組",
        "groups_and_ids": "群組及 ID:",
        "group_members": "群組 {group_id} 的成員:",
        "no_members": "沒有成員",
        "err_unknown_command": "未知指令: {list_token}",
        "recent_messages_with": "與 {friend_id} 的最近訊息:",
        "no_messages": "找不到訊息。",
        "recent_group_messages_in": "群組 {group_id} 的最近訊息:",
        "no_group_messages": "找不到群組訊息。",
        "unread_private_messages": "未讀私聊訊息:",
        "no_unread_messages": "沒有未讀訊息",
        "err_msg_empty": "訊息內容為空",
        "message_sent_to": "訊息已傳送給 {friend_id}。",
        "group_message_sent_to": "群組訊息已傳送到 {group_id}。",
        "friend_request_sent_to": "好友邀請已傳送給 {user_id}。",
        "err_need_user_id": "至少需要一個使用者 ID",
        "invited_to_group": "已邀請 {user_ids} 加入群組 {group_id}。",
        "err_unknown_add_target": "未知的 add 目標: {sub}",
        "friend_deleted": "好友 {user_id} 已刪除。",
        "removed_from_group": "已將 {user_ids} 移出群組 {group_id}。",
        "err_unknown_del_target": "未知的 del 目標: {sub}",
        "err_group_name_empty": "群組名稱為空",
        "group_created": "群組已建立: id={group_id} name={group_name}",
        "err_unknown_new_target": "未知的 new 目標: {sub}",
        "group_deleted": "群組 {group_id} 已刪除。",
        "user_muted_in_group": "使用者 {user_id} 已在群組 {group_id} 中被禁言。",
        "user_unmuted_in_group": "使用者 {user_id} 已在群組 {group_id} 中解除禁言。",
        "group_flag_set": "群組 {group_id} 的 {sub} 已設定為 {flag}。",
        "err_name_empty": "名稱為空",
        "group_name_updated": "群組 {group_id} 名稱已更新。",
        "group_notice_updated": "群組 {group_id} 公告已更新。",
        "err_unknown_set_option": "未知的 set 選項: {sub}",
        "err_unknown_mygroup_action": "未知的 mygroup 操作: {action}",
        "err_remark_empty": "備註內容為空",
        "group_remark_updated": "群組 {group_id} 備註已更新。",
        "err_unknown_groups_set_option": "未知的 groups set 選項: {option}",
        "err_unknown_groups_action": "未知的 groups 操作: {sub}",
        "err_user_not_found": "使用者 {friend_id} 不存在",
        "user_card_sent_to_friend": "已將使用者 {friend_id} 的名片傳送給好友 {target_friend_id}。",
        "user_card_sent_to_group": "已將使用者 {friend_id} 的名片傳送到群組 {group_id}。",
        "err_unknown_recommend_target": "未知的 recommend 目標: {target}",
        "help_available": "可用指令:",
        "help_whoami": "顯示目前登入的使用者名稱和密碼",
        "help_login": "登入帳號，無參數則逐項輸入",
        "help_sign": "註冊帳號，無參數則逐項輸入",
        "help_exit": "退出程式",
        "help_list_friends": "列出好友",
        "help_list_groups": "列出群組",
        "help_get_history": "檢視私聊歷史訊息",
        "help_get_ghistory": "檢視群組歷史訊息",
        "help_get_unread": "檢視未讀私聊訊息",
        "help_send": "傳送私聊訊息",
        "help_gsend": "傳送群組訊息",
        "help_add_friend": "傳送好友邀請",
        "help_add_group": "邀請使用者加入群組",
        "help_del_friend": "刪除好友",
        "help_del_group": "將使用者移出群組",
        "help_new_group": "建立群組",
        "help_mygroup_del_this": "解散群組",
        "help_mygroup_mute": "禁言使用者",
        "help_mygroup_unmute": "解除禁言",
        "help_mygroup_set_flag": "設定群組開關",
        "help_mygroup_set_name": "修改群組名稱",
        "help_mygroup_set_notice": "修改群組公告",
        "help_groups_set": "設定群組備註名",
        "help_groups_list": "顯示群成員列表",
        "help_recommend_friend": "傳送使用者名片給好友",
        "help_recommend_group": "傳送使用者名片到群組",
        "help_cls": "清空畫面",
        "unknown_time": "未知時間",
    },
}


def tr(key):
    return I18N.get(LANG, I18N["zh"]).get(key, I18N["zh"].get(key, key))


try:
    import boxim
except ImportError:
    print(f"{RED}[Error]{END}{tr('err_no_sdk')}")
    print(tr('update_pip'))
    os.system("python.exe -m pip install --upgrade pip")
    print(tr('download_sdk'))
    os.system("python.exe -m pip install boxim-sdk")

user_name = ""
user_password = ""


def try_auto_login():
    global user_name
    client = None
    try:
        client = boxim.BoxIM()
        token = client.token_store.get_token()
        if token and (token.access_token or token.refresh_token):
            me = client.get_me()
            user_name = str(me.get("userName") or me.get("nickName") or me.get("id") or "")
            boxim.register(client)
            return True
        client.close()
        return False
    except Exception:
        if client is not None:
            try:
                client.close()
            except Exception:
                pass
        return False


if try_auto_login():
    print(f"{GREEN}{tr('auto_login_success')} {user_name}{END}")
else:
    print(f"{BLUE}{tr('login_to_boxim')}{END}")
    user_name = input(tr('input_user_name'))
    user_password = getpass.getpass(tr('input_user_password'))
    user = boxim.init(user_name, user_password)

user = boxim.get()

friends:list = boxim.get_friends()
groups:list = boxim.get_groups()

tokens:list = []


def format_timestamp(millis):
    try:
        millis = int(millis)
    except (TypeError, ValueError):
        return tr("unknown_time")
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(millis / 1000))


class Command:
    def __init__(self):
        global user
        global user_name
        global user_password
        global tokens
        global friends
        global groups
        return

    def whoami(self):
        print(f"{BLUE}{tr('user_name_label')}{GREEN}{user_name}{END}")
        print(f"{BLUE}{tr('user_password_label')}{GREEN}{user_password}{END}")
        return

    def cls(self):
        os.system("cls")
        return

    def login(self, token_number):
        global user
        global user_name
        global user_password
        global friends
        global groups
        if len(tokens) == token_number + 1:
            print(f"{BLUE}{tr('login_to_boxim')}{END}")
            user_name = input(tr('input_user_name'))
            user_password = getpass.getpass(tr('input_user_password'))
        else:
            user_name = tokens[token_number + 1]
            user_password = tokens[token_number + 2]
        print(f"{BLUE}{tr('login_doing')}{END}")
        user = boxim.init(user_name, user_password)
        user = boxim.get()
        friends = boxim.get_friends()
        groups = boxim.get_groups()
        return

    def sign(self, token_number):
        global user
        global user_name
        global user_password
        global friends
        global groups
        if len(tokens) == token_number + 1:
            print(f"{BLUE}{tr('sign_to_boxim')}{END}")
            user_name = input(tr('input_user_name'))
            user_password = getpass.getpass(tr('input_user_password'))
        else:
            user_name = tokens[token_number + 1]
            user_password = tokens[token_number + 2]
        print(f"{BLUE}{tr('sign_doing')}{END}")
        user.register(
            boxim.RegistrationMode.USERNAME,
            user_name=user_name,
            password=user_password,
            confirm_password=user_password,
        )
        print(f"{GREEN}{tr('sign_success')}{END}")
        user = boxim.init(user_name, user_password)
        user = boxim.get()
        friends = boxim.get_friends()
        groups = boxim.get_groups()
        print(f"{BLUE}{tr('login_success')}{END}")
        return

    def exit(self, token_number):
        if len(tokens) == token_number + 1:
            exit(0)
        else:
            try:
                exit(int(tokens[token_number + 1]))
            except (TypeError, ValueError):
                print(f"{RED}[Error]{END}{tr('err_exit_int')}")
        return

    def list(self, token_number):
        global friends
        global groups
        list_token = tokens[token_number + 1]

        match list_token:
            case "friends":
                friends = boxim.get_friends()
                if not friends:
                    print(f"{YELLOW}{tr('no_friends')}{END}")
                    return
                max_name_len = max(len(friend.nick_name) for friend in friends)
                max_id_len = max(len(str(friend.id)) for friend in friends)
                print(f"{BLUE}{tr('friends_and_ids')}{END}")
                for friend in friends:
                    print(f"{BLUE}{tr('id_label')}: {friend.id:<{max_id_len}} {tr('name_label')}: {friend.nick_name:<{max_name_len}}{END}")
            case "groups":
                groups = boxim.get_groups()
                if not groups:
                    print(f"{YELLOW}{tr('no_groups')}{END}")
                    return
                print(f"{BLUE}{tr('groups_and_ids')}{END}")
                max_name_len = max(len(group.name) for group in groups)
                max_id_len = max(len(str(group.id)) for group in groups)
                for group in groups:
                    print(f"{BLUE}{tr('id_label')}: {group.id:<{max_id_len}} {tr('name_label')}: {group.name:<{max_name_len}}{END}")
            case _:
                print(f"{RED}[Error]{END}{tr('err_unknown_command').format(list_token=list_token)}")
        return

    def get(self, token_number):
        get_token = tokens[token_number + 1]
        match get_token:
            case "history":
                friend_id = int(tokens[token_number + 2])
                count = 30
                if len(tokens) > token_number + 3:
                    count = int(tokens[token_number + 3])
                messages = user.load_private_offline_message(0)
                related = [
                    msg for msg in messages
                    if msg.get('sendId') == friend_id or msg.get('recvId') == friend_id
                ]
                related.sort(key=lambda msg: msg.get('sendTime') or 0)
                recent = related[-count:]
                if recent:
                    print(f"{BLUE}{tr('recent_messages_with').format(friend_id=friend_id)}{END}")
                    for msg in recent:
                        sender_id = msg.get('sendId')
                        nick_name = msg.get('sendNickName')
                        content = msg.get('content')
                        send_time = format_timestamp(msg.get('sendTime'))
                        if nick_name:
                            print(f"{BLUE}[{send_time}]{END} {GREEN}{nick_name}({sender_id}){END}: {content}")
                        else:
                            print(f"{BLUE}[{send_time}]{END} {GREEN}{sender_id}{END}: {content}")
                else:
                    print(f"{YELLOW}{tr('no_messages')}{END}")
            case "ghistory":
                group_id = int(tokens[token_number + 2])
                count = 30
                if len(tokens) > token_number + 3:
                    count = int(tokens[token_number + 3])
                messages = user.load_group_offline_message(0)
                related = [
                    msg for msg in messages
                    if msg.get('groupId') == group_id
                ]
                related.sort(key=lambda msg: msg.get('sendTime') or 0)
                recent = related[-count:]
                recent.reverse()
                if recent:
                    print(f"{BLUE}{tr('recent_group_messages_in').format(group_id=group_id)}{END}")
                    for msg in recent:
                        sender_id = msg.get('sendId')
                        nick_name = msg.get('sendNickName')
                        content = msg.get('content')
                        send_time = format_timestamp(msg.get('sendTime'))
                        if nick_name:
                            print(f"{BLUE}[{send_time}]{END} {GREEN}{nick_name}({sender_id}){END}: {content}")
                        else:
                            print(f"{BLUE}[{send_time}]{END} {GREEN}{sender_id}{END}: {content}")
                else:
                    print(f"{YELLOW}{tr('no_group_messages')}{END}")
            case "unread":
                my_id = user.me['id']
                friend_filter = None
                if len(tokens) > token_number + 2:
                    friend_filter = int(tokens[token_number + 2])
                messages = user.load_private_offline_message(0)
                unread = [
                    msg for msg in messages
                    if msg.get('sendId') != my_id and msg.get('status') == 1
                ]
                if friend_filter is not None:
                    unread = [
                        msg for msg in unread
                        if msg.get('sendId') == friend_filter
                    ]
                unread.sort(key=lambda msg: msg.get('sendTime') or 0)
                if unread:
                    print(f"{BLUE}{tr('unread_private_messages')}{END}")
                    for msg in unread:
                        sender_id = msg.get('sendId')
                        nick_name = msg.get('sendNickName')
                        content = msg.get('content')
                        send_time = format_timestamp(msg.get('sendTime'))
                        if nick_name:
                            print(f"{BLUE}[{send_time}]{END} {GREEN}{nick_name}({sender_id}){END}: {content}")
                        else:
                            print(f"{BLUE}[{send_time}]{END} {GREEN}{sender_id}{END}: {content}")
                else:
                    print(f"{YELLOW}{tr('no_unread_messages')}{END}")

    def send(self, token_number):
        friend_id = int(tokens[token_number + 1])
        text = " ".join(tokens[token_number + 2:])
        if not text:
            print(f"{RED}[Error]{END}{tr('err_msg_empty')}")
            return
        user.send_text(friend_id, text)
        print(f"{GREEN}{tr('message_sent_to').format(friend_id=friend_id)}{END}")

    def gsend(self, token_number):
        group_id = int(tokens[token_number + 1])
        text = " ".join(tokens[token_number + 2:])
        if not text:
            print(f"{RED}[Error]{END}{tr('err_msg_empty')}")
            return
        user.send_group_text(group_id, text)
        print(f"{GREEN}{tr('group_message_sent_to').format(group_id=group_id)}{END}")

    def add(self, token_number):
        sub = tokens[token_number + 1]
        if sub == "friend":
            user_id = int(tokens[token_number + 2])
            remark = " ".join(tokens[token_number + 3:]) or None
            user.add_friend(user_id, remark)
            print(f"{GREEN}{tr('friend_request_sent_to').format(user_id=user_id)}{END}")
        elif sub == "group":
            group_id = int(tokens[token_number + 2])
            user_ids = [int(x) for x in tokens[token_number + 3:]]
            if not user_ids:
                print(f"{RED}[Error]{END}{tr('err_need_user_id')}")
                return
            user.invite_to_group(group_id, user_ids)
            print(f"{GREEN}{tr('invited_to_group').format(user_ids=user_ids, group_id=group_id)}{END}")
        else:
            print(f"{RED}[Error]{END}{tr('err_unknown_add_target').format(sub=sub)}")
        return

    def del_(self, token_number):
        sub = tokens[token_number + 1]
        if sub == "friend":
            user_id = int(tokens[token_number + 2])
            user.delete_friend(user_id)
            print(f"{GREEN}{tr('friend_deleted').format(user_id=user_id)}{END}")
        elif sub == "group":
            group_id = int(tokens[token_number + 2])
            user_ids = [int(x) for x in tokens[token_number + 3:]]
            if not user_ids:
                print(f"{RED}[Error]{END}{tr('err_need_user_id')}")
                return
            user.remove_group_members(group_id, user_ids)
            print(f"{GREEN}{tr('removed_from_group').format(user_ids=user_ids, group_id=group_id)}{END}")
        else:
            print(f"{RED}[Error]{END}{tr('err_unknown_del_target').format(sub=sub)}")
        return

    def new(self, token_number):
        sub = tokens[token_number + 1]
        if sub == "group":
            name = " ".join(tokens[token_number + 2:])
            if not name:
                print(f"{RED}[Error]{END}{tr('err_group_name_empty')}")
                return
            group = user.create_group(name)
            print(f"{GREEN}{tr('group_created').format(group_id=group.id, group_name=group.name)}{END}")
        else:
            print(f"{RED}[Error]{END}{tr('err_unknown_new_target').format(sub=sub)}")
        return

    def mygroup(self, token_number):
        group_id = int(tokens[token_number + 1])
        action = tokens[token_number + 2]

        if action == "add":
            user_ids = [int(x) for x in tokens[token_number + 3:]]
            if not user_ids:
                print(f"{RED}[Error]{END}{tr('err_need_user_id')}")
                return
            user.invite_to_group(group_id, user_ids)
            print(f"{GREEN}{tr('invited_to_group').format(user_ids=user_ids, group_id=group_id)}{END}")
            return

        if action == "del":
            if tokens[token_number + 3] == "this":
                user.delete_group(group_id)
                print(f"{GREEN}{tr('group_deleted').format(group_id=group_id)}{END}")
            else:
                user_ids = [int(x) for x in tokens[token_number + 3:]]
                user.remove_group_members(group_id, user_ids)
                print(f"{GREEN}{tr('removed_from_group').format(user_ids=user_ids, group_id=group_id)}{END}")
            return

        if action == "mute":
            user_id = int(tokens[token_number + 3])
            user.set_group_member_muted(group_id, [user_id], True)
            print(f"{GREEN}{tr('user_muted_in_group').format(user_id=user_id, group_id=group_id)}{END}")
            return

        if action == "unmute":
            user_id = int(tokens[token_number + 3])
            user.set_group_member_muted(group_id, [user_id], False)
            print(f"{GREEN}{tr('user_unmuted_in_group').format(user_id=user_id, group_id=group_id)}{END}")
            return

        if action == "set":
            sub = tokens[token_number + 3]
            if sub in ("muted", "allowInvite", "allowShareCard"):
                flag = tokens[token_number + 4].lower() == "on"
                if sub == "muted":
                    user.set_group_muted(group_id, flag)
                elif sub == "allowInvite":
                    user.set_group_allow_invite(group_id, flag)
                else:
                    user.set_group_allow_share_card(group_id, flag)
                print(f"{GREEN}{tr('group_flag_set').format(group_id=group_id, sub=sub, flag=flag)}{END}")
            elif sub == "name":
                text = " ".join(tokens[token_number + 4:])
                if not text:
                    print(f"{RED}[Error]{END}{tr('err_name_empty')}")
                    return
                user.modify_group(group_id, name=text)
                print(f"{GREEN}{tr('group_name_updated').format(group_id=group_id)}{END}")
            elif sub == "notice":
                text = " ".join(tokens[token_number + 4:])
                user.modify_group(group_id, notice=text)
                print(f"{GREEN}{tr('group_notice_updated').format(group_id=group_id)}{END}")
            else:
                print(f"{RED}[Error]{END}{tr('err_unknown_set_option').format(sub=sub)}")
            return

        print(f"{RED}[Error]{END}{tr('err_unknown_mygroup_action').format(action=action)}")
        return

    def groups(self, token_number):
        sub = tokens[token_number + 1]
        if sub == "set":
            option = tokens[token_number + 3]
            if option == "remark":
                group_id = int(tokens[token_number + 2])
                text = " ".join(tokens[token_number + 4:])
                if not text:
                    print(f"{RED}[Error]{END}{tr('err_remark_empty')}")
                    return
                user.modify_group(group_id, remarkGroupName=text)
                print(f"{GREEN}{tr('group_remark_updated').format(group_id=group_id)}{END}")
            else:
                print(f"{RED}[Error]{END}{tr('err_unknown_groups_set_option').format(option=option)}")
        elif sub.isdigit() and len(tokens) > token_number + 2 and tokens[token_number + 2] == "list":
            group_id = int(sub)
            members = user.get_group_members(group_id)
            if not members:
                print(f"{YELLOW}{tr('no_members')}{END}")
                return
            print(f"{BLUE}{tr('group_members').format(group_id=group_id)}{END}")
            for member in members:
                print(f"{BLUE}{tr('id_label')}: {member.id} {tr('name_label')}: {member.nick_name}{END}")
        else:
            print(f"{RED}[Error]{END}{tr('err_unknown_groups_action').format(sub=sub)}")
        return

    def recommend(self, token_number):
        target = tokens[token_number + 1]
        friend_id = int(tokens[token_number + 2])
        friend = user.get_user(friend_id)
        if friend is None:
            print(f"{RED}[Error]{END}{tr('err_user_not_found').format(friend_id=friend_id)}")
            return
        nick = friend.nick_name
        head = friend.head_image
        if target == "friend":
            target_friend_id = int(tokens[token_number + 3])
            user.send_user_card(target_friend_id, friend_id, nick, head)
            print(f"{GREEN}{tr('user_card_sent_to_friend').format(friend_id=friend_id, target_friend_id=target_friend_id)}{END}")
        elif target == "group":
            group_id = int(tokens[token_number + 3])
            content = boxim.MessageBuilder.user_card(friend_id, nick, head)
            user._send_group_message(group_id, content, boxim.MessageType.USER_CARD)
            print(f"{GREEN}{tr('user_card_sent_to_group').format(friend_id=friend_id, group_id=group_id)}{END}")
        else:
            print(f"{RED}[Error]{END}{tr('err_unknown_recommend_target').format(target=target)}")
        return

    def help(self):
        print(f"{BLUE}{tr('help_available')}{END}")
        print(f"{GREEN}whoami:{END}{BLUE}    {tr('help_whoami')}{END}")
        print(f"{GREEN}login [user password]:{END}{BLUE}    {tr('help_login')}{END}")
        print(f"{GREEN}sign [name password]:{END}{BLUE}    {tr('help_sign')}{END}")
        print(f"{GREEN}exit [code]:{END}{BLUE}    {tr('help_exit')}{END}")
        print(f"{GREEN}list:{END}")
        print(f"{GREEN}    friends:{END}{BLUE}    {tr('help_list_friends')}{END}")
        print(f"{GREEN}    groups:{END}{BLUE}    {tr('help_list_groups')}{END}")
        print(f"{GREEN}get:{END}")
        print(f"{GREEN}    history <friend_id> [count]:{END}{BLUE}    {tr('help_get_history')}{END}")
        print(f"{GREEN}    ghistory <group_id> [count]:{END}{BLUE}    {tr('help_get_ghistory')}{END}")
        print(f"{GREEN}    unread [friend_id]:{END}{BLUE}    {tr('help_get_unread')}{END}")
        print(f"{GREEN}send <friend_id> <text>:{END}{BLUE}    {tr('help_send')}{END}")
        print(f"{GREEN}gsend <group_id> <text>:{END}{BLUE}    {tr('help_gsend')}{END}")
        print(f"{GREEN}add:{END}")
        print(f"{GREEN}    friend <user_id> [remark]:{END}{BLUE}    {tr('help_add_friend')}{END}")
        print(f"{GREEN}    group <group_id> <user_id> [...]:{END}{BLUE}    {tr('help_add_group')}{END}")
        print(f"{GREEN}del:{END}")
        print(f"{GREEN}    friend <user_id>:{END}{BLUE}    {tr('help_del_friend')}{END}")
        print(f"{GREEN}    group <group_id> <user_id> [...]:{END}{BLUE}    {tr('help_del_group')}{END}")
        print(f"{GREEN}new:{END}")
        print(f"{GREEN}    group <name>:{END}{BLUE}    {tr('help_new_group')}{END}")
        print(f"{GREEN}mygroup <group_id>:{END}")
        print(f"{GREEN}    add <user_id> [...]:{END}{BLUE}    {tr('help_add_group')}{END}")
        print(f"{GREEN}    del this:{END}{BLUE}    {tr('help_mygroup_del_this')}{END}")
        print(f"{GREEN}    del <user_id> [...]:{END}{BLUE}    {tr('help_del_group')}{END}")
        print(f"{GREEN}    mute <user_id>:{END}{BLUE}    {tr('help_mygroup_mute')}{END}")
        print(f"{GREEN}    unmute <user_id>:{END}{BLUE}    {tr('help_mygroup_unmute')}{END}")
        print(f"{GREEN}    set muted|allowInvite|allowShareCard on|off:{END}{BLUE}    {tr('help_mygroup_set_flag')}{END}")
        print(f"{GREEN}    set name <text>:{END}{BLUE}    {tr('help_mygroup_set_name')}{END}")
        print(f"{GREEN}    set notice <text>:{END}{BLUE}    {tr('help_mygroup_set_notice')}{END}")
        print(f"{GREEN}groups:{END}")
        print(f"{GREEN}    list <group_id>:{END}{BLUE}    {tr('help_groups_list')}{END}")
        print(f"{GREEN}    set <group_id> remark <text>:{END}{BLUE}    {tr('help_groups_set')}{END}")
        print(f"{GREEN}recommend:{END}")
        print(f"{GREEN}    friend <friend_id> <target_friend_id>:{END}{BLUE}    {tr('help_recommend_friend')}{END}")
        print(f"{GREEN}    group <friend_id> <group_id>:{END}{BLUE}    {tr('help_recommend_group')}{END}")
        print(f"{GREEN}cls:{END}{BLUE}    {tr('help_cls')}{END}")
        return


def run_command(command_tokens):
    global tokens
    global LANG
    tokens = list(command_tokens)
    filtered = []
    i = 0
    while i < len(tokens):
        if tokens[i] == "-l" and i + 1 < len(tokens) and tokens[i + 1] in ("zh", "en", "tw"):
            LANG = tokens[i + 1]
            i += 2
            continue
        filtered.append(tokens[i])
        i += 1
    tokens = filtered
    if not tokens:
        return
    command = Command()
    token_number = 0
    token = tokens[0]

    try:
        match token:
                case "whoami":
                    command.whoami()
                case "login":
                    command.login(token_number)
                case "exit":
                    command.exit(token_number)
                case "list":
                    command.list(token_number)
                case "get":
                    command.get(token_number)
                case "send":
                    command.send(token_number)
                case "gsend":
                    command.gsend(token_number)
                case "sign":
                    command.sign(token_number)
                case "cls":
                    command.cls()
                case "help":
                    command.help()
                case "add":
                    command.add(token_number)
                case "del":
                    command.del_(token_number)
                case "new":
                    command.new(token_number)
                case "mygroup":
                    command.mygroup(token_number)
                case "groups":
                    command.groups(token_number)
                case "recommend":
                    command.recommend(token_number)
    except SystemExit:
        raise
    except Exception as e:
        print(f"{RED}[Error]{END}{str(e)}")


def main():
    args = sys.argv[1:]
    if args:
        run_command(args)
    else:
        while True:
            try:
                line = input(f"{GREEN}boxim-cmd/>{BLUE}${END} ")
            except (EOFError, KeyboardInterrupt):
                break
            run_command(line.split())


if __name__ == "__main__":
    main()
#https://github.com/foxange-org/boxim-cmd
#制作者 : SLC_Extreme