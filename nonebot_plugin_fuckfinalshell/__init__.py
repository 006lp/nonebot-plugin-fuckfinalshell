from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.params import CommandArg
from nonebot.plugin import PluginMetadata
from nonebot.adapters import Message
from Crypto.Hash import MD5, keccak

__plugin_meta__ = PluginMetadata(
    name="FinalShell 离线激活码",
    description="FinalShell Offline Activation Code",
    usage="/fskey xxx",
    type="application",
    homepage="https://github.com/006lp/nonebot-plugin-fuckfinalshell",
    supported_adapters=None
)


# --- 核心计算逻辑 ---

def calc_md5(data: str) -> str:
    return MD5.new(data.encode()).hexdigest()

def calc_keccak384(data: str) -> str:
    return keccak.new(data=data.encode(), digest_bits=384).hexdigest()

def generate_activation_codes(machine_id: str) -> str:
    
    # FinalShell < 3.9.6
    fs_lt_396_adv = calc_md5(f'61305{machine_id}8552')[8:24]
    fs_lt_396_pro = calc_md5(f'2356{machine_id}13593')[8:24]

    # FinalShell >= 3.9.6
    fs_ge_396_adv = calc_keccak384(f'{machine_id}hSf(78cvVlS5E')[12:28]
    fs_ge_396_pro = calc_keccak384(f'{machine_id}FF3Go(*Xvbb5s2')[12:28]

    # FinalShell 4.5
    fs_4_5_adv = calc_keccak384(f'{machine_id}wcegS3gzA$')[12:28]
    fs_4_5_pro = calc_keccak384(f'{machine_id}b(xxkHn%z);x')[12:28]
    
    # FinalShell 4.6
    fs_4_6_adv = calc_keccak384(f'{machine_id}csSf5*xlkgYSX,y')[12:28]
    fs_4_6_pro = calc_keccak384(f'{machine_id}Scfg*ZkvJZc,s,Y')[12:28]

    response_text = f"""
为机器码 {machine_id} 生成的激活码如下：

FinalShell < 3.9.6
🟡 高级版: {fs_lt_396_adv}
🟢 专业版: {fs_lt_396_pro}

FinalShell ≥ 3.9.6
🟡 高级版: {fs_ge_396_adv}
🟢 专业版: {fs_ge_396_pro}

FinalShell 4.5
🟡 高级版: {fs_4_5_adv}
🟢 专业版: {fs_4_5_pro}

FinalShell 4.6
🟡 高级版: {fs_4_6_adv}
🟢 专业版: {fs_4_6_pro}
""".strip()
    
    return response_text


fs_key_generator = on_command("fskey", aliases={"finalshellkey"}, priority=85, block=True)

@fs_key_generator.handle()
async def handle_fskey_command(matcher: Matcher, args: Message = CommandArg()):

    # 使用 extract_plain_text() 获取纯文本形式的参数
    machine_id = args.extract_plain_text().strip()

    # 检查用户是否输入了机器码
    if not machine_id:
        await matcher.finish("请输入机器码，例如：/fskey xxx")

    try:
        result_text = generate_activation_codes(machine_id)
        await matcher.send(result_text)
    except Exception as e:
        await matcher.send(f"生成激活码时出错: {e}")