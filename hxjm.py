import os
import sys
import json
import random
import time
import shutil
import re
import base64
import socket
import subprocess
import platform
from datetime import datetime
import uuid
from pathlib import Path
import urllib.request
import ssl
import tempfile
import argparse
INSTALL_DIR = Path.home() / '.mulu'
CONFIG_FILE = INSTALL_DIR / 'config.json'
SB_PID_FILE = INSTALL_DIR / 'sbpid.log'
zmk_PID_FILE = INSTALL_DIR / 'sbzmkpid.log'
LIST_FILE = INSTALL_DIR / 'list.txt'
LOG_FILE = INSTALL_DIR / 'zmk.log'
DEBUG_LOG = INSTALL_DIR / 'python_debug.log'
CUSTOM_DOMAIN_FILE = INSTALL_DIR / 'custom_domain.txt'
USER_NAME = 'gdljlj'
UUID = '2faaf996-d2b0-440d-8258-81f2b05dd0e4'
PORT = 49999
DOMAIN = 'jm.xwm.dpdns.org'
TOKEN = 'eyJhIjoiOGRmYzUzODAwYmQ5NGQwZjYzMDNkMGUzNzA4Y2IxMjUiLCJ0IjoiZDA3YWIwNDctYzNkYy00MTlhLTkyNzAtMDY0YjQxYTI2Nzg0IiwicyI6IlpEYzFZakptWkRZdE16TTBNUzAwWkdKaUxUazVNV1V0WmpnMk1tTXpNR001WlRWbSJ9'
def ArDBdoLK():
    parser = argparse.ArgumentParser(description='zmkSB Python3 一键脚本 (支持自定义域名和zmk Token)')
    parser.add_argument('action', nargs='?', default='install', choices=['install', 'status', 'update', 'del', 'uninstall', 'cat'], help='操作类型: install(安装), status(状态), update(更新), del(卸载), cat(查看节点)')
    parser.add_argument('--domain', '-d', dest='agn', help='设置自定义域名 (例如: xxx.trycloudflare.com 或 your.custom.domain)')
    parser.add_argument('--uuid', '-u', help='设置自定义UUID')
    parser.add_argument('--port', '-p', dest='vmpt', type=int, help='设置自定义Vmess端口')
    parser.add_argument('--agk', '--token', dest='agk', help='设置 zmk Tunnel Token (用于Cloudflare Zero Trust命名隧道)')
    parser.add_argument('--user', '-U', dest='user', help='设置用户名（用于上传文件名）')
    return parser.parse_args()
def PqwoBLeg(LFIyVxVB, TgFxYRmx=10):
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        req = urllib.request.Request(LFIyVxVB, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=TgFxYRmx) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        print(f'HTTP请求失败: {LFIyVxVB}, 错误: {e}')
        write_debug_log(f'HTTP GET Error: {LFIyVxVB}, {e}')
        return None
def IodVTEsP(LFIyVxVB, VIEoZhml, EtWzABej='wb'):
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        req = urllib.request.Request(LFIyVxVB, headers=headers)
        with urllib.request.urlopen(req, context=ctx) as response, open(VIEoZhml, EtWzABej) as out_file:
            shutil.copyfileobj(response, out_file)
        return True
    except Exception as e:
        print(f'下载文件失败: {LFIyVxVB}, 错误: {e}')
        write_debug_log(f'Download Error: {LFIyVxVB}, {e}')
        return False
def ftlEtxzv():
    print('\x1b[36m╭───────────────────────────────────────────────────────────────╮\x1b[0m')
    print('\x1b[36m│             \x1b[33m✨ zmkSB Python3 自定义域名版 ✨              \x1b[36m│\x1b[0m')
    print('\x1b[36m├───────────────────────────────────────────────────────────────┤\x1b[0m')
    print('\x1b[36m│ \x1b[32m作者: 康康                                                  \x1b[36m│\x1b[0m')
    print('\x1b[36m│ \x1b[32mGithub: https://github.com/zhumengkang/                    \x1b[36m│\x1b[0m')
    print('\x1b[36m│ \x1b[32mYouTube: https://www.youtube.com/@康康的V2Ray与Clash         \x1b[36m│\x1b[0m')
    print('\x1b[36m│ \x1b[32mTelegram: https://t.me/+WibQp7Mww1k5MmZl                   \x1b[36m│\x1b[0m')
    print('\x1b[36m│ \x1b[32m版本: 25.7.0 (支持zmk Token及交互式输入)                 \x1b[36m│\x1b[0m')
    print('\x1b[36m╰───────────────────────────────────────────────────────────────╯\x1b[0m')
def DpsifjYV():
    print('\x1b[33m使用方法:\x1b[0m')
    print('  \x1b[36mpython3 script.py\x1b[0m                     - 交互式安装或启动服务')
    print('  \x1b[36mpython3 script.py install\x1b[0m             - 安装服务 (可配合参数)')
    print('  \x1b[36mpython3 script.py --agn example.com\x1b[0m   - 使用自定义域名安装')
    print('  \x1b[36mpython3 script.py --uuid YOUR_UUID\x1b[0m      - 使用自定义UUID安装')
    print('  \x1b[36mpython3 script.py --vmpt 12345\x1b[0m         - 使用自定义端口安装')
    print('  \x1b[36mpython3 script.py --agk YOUR_TOKEN\x1b[0m     - 使用zmk Tunnel Token安装')
    print('  \x1b[36mpython3 script.py status\x1b[0m              - 查看服务状态和节点信息')
    print('  \x1b[36mpython3 script.py cat\x1b[0m                 - 查看单行节点列表')
    print('  \x1b[36mpython3 script.py update\x1b[0m              - 更新脚本')
    print('  \x1b[36mpython3 script.py del\x1b[0m                 - 卸载服务')
    print()
    print('\x1b[33m支持的环境变量:\x1b[0m')
    print('  \x1b[36mexport vmpt=12345\x1b[0m                       - 设置自定义Vmess端口')
    print('  \x1b[36mexport uuid=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx\x1b[0m - 设置自定义UUID')
    print('  \x1b[36mexport agn=your-domain.com\x1b[0m              - 设置自定义域名')
    print('  \x1b[36mexport agk=YOUR_zmk_TUNNEL_TOKEN\x1b[0m       - 设置zmk Tunnel Token')
    print()
def xBDTVlNP(YmPQXluG):
    try:
        if not INSTALL_DIR.exists():
            INSTALL_DIR.mkdir(parents=True, exist_ok=True)
        with open(DEBUG_LOG, 'a', encoding='utf-8') as f:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write(f'[{timestamp}] {YmPQXluG}\n')
    except Exception as e:
        print(f'写入日志失败: {e}')
def MCrxYCAL(pKBTzNXB, ogGcJzMB, VIEoZhml):
    print(f'正在下载 {pKBTzNXB}...')
    success = IodVTEsP(ogGcJzMB, VIEoZhml)
    if success:
        print(f'{pKBTzNXB} 下载成功!')
        os.chmod(VIEoZhml, 493)
        return True
    else:
        print(f'{pKBTzNXB} 下载失败!')
        return False
def DnyKDzbr(oGyPUvNC):
    vmess_obj = {'v': '2', 'ps': oGyPUvNC.get('ps', 'zmkSB'), 'add': oGyPUvNC.get('add', ''), 'port': str(oGyPUvNC.get('port', '443')), 'id': oGyPUvNC.get('id', ''), 'aid': str(oGyPUvNC.get('aid', '0')), 'net': oGyPUvNC.get('net', 'ws'), 'type': oGyPUvNC.get('type', 'none'), 'host': oGyPUvNC.get('host', ''), 'path': oGyPUvNC.get('path', ''), 'tls': oGyPUvNC.get('tls', 'tls'), 'sni': oGyPUvNC.get('sni', '')}
    vmess_str = json.dumps(vmess_obj, sort_keys=True)
    vmess_b64 = base64.b64encode(vmess_str.encode('utf-8')).decode('utf-8').rstrip('=')
    return f'vmess://{vmess_b64}'
def JwWhaYvn(SjMfcthz, MuvcCifw, nmOqgIjq):
    xBDTVlNP(f'生成链接: domain={SjMfcthz}, port_vm_ws={MuvcCifw}, uuid_str={nmOqgIjq}')
    ws_path = f'/{nmOqgIjq[:8]}-vm'
    ws_path_full = f'{ws_path}?ed=2048'
    xBDTVlNP(f'WebSocket路径: {ws_path_full}')
    hostname = socket.gethostname()[:10]
    all_links = []
    link_names = []
    link_configs_for_json_output = []
    cf_ips_tls = {'104.16.0.0': '443', '104.17.0.0': '8443', '104.18.0.0': '2053', '104.19.0.0': '2083', '104.20.0.0': '2087'}
    cf_ips_http = {'104.21.0.0': '80', '104.22.0.0': '8080', '104.24.0.0': '8880'}
    for ip, port_cf in cf_ips_tls.items():
        ps_name = f"VMWS-TLS-{hostname}-{ip.split('.')[2]}-{port_cf}"
        oGyPUvNC = {'ps': ps_name, 'add': ip, 'port': port_cf, 'id': nmOqgIjq, 'aid': '0', 'net': 'ws', 'type': 'none', 'host': SjMfcthz, 'path': ws_path_full, 'tls': 'tls', 'sni': SjMfcthz}
        all_links.append(DnyKDzbr(oGyPUvNC))
        link_names.append(f'TLS-{port_cf}-{ip}')
        link_configs_for_json_output.append(oGyPUvNC)
    for ip, port_cf in cf_ips_http.items():
        ps_name = f"VMWS-HTTP-{hostname}-{ip.split('.')[2]}-{port_cf}"
        oGyPUvNC = {'ps': ps_name, 'add': ip, 'port': port_cf, 'id': nmOqgIjq, 'aid': '0', 'net': 'ws', 'type': 'none', 'host': SjMfcthz, 'path': ws_path_full, 'tls': ''}
        all_links.append(DnyKDzbr(oGyPUvNC))
        link_names.append(f'HTTP-{port_cf}-{ip}')
        link_configs_for_json_output.append(oGyPUvNC)
    direct_tls_config = {'ps': f'VMWS-TLS-{hostname}-Direct-{SjMfcthz[:15]}-443', 'add': SjMfcthz, 'port': '443', 'id': nmOqgIjq, 'aid': '0', 'net': 'ws', 'type': 'none', 'host': SjMfcthz, 'path': ws_path_full, 'tls': 'tls', 'sni': SjMfcthz}
    all_links.append(DnyKDzbr(direct_tls_config))
    link_names.append(f'TLS-Direct-{SjMfcthz}-443')
    link_configs_for_json_output.append(direct_tls_config)
    direct_http_config = {'ps': f'VMWS-HTTP-{hostname}-Direct-{SjMfcthz[:15]}-80', 'add': SjMfcthz, 'port': '80', 'id': nmOqgIjq, 'aid': '0', 'net': 'ws', 'type': 'none', 'host': SjMfcthz, 'path': ws_path_full, 'tls': ''}
    all_links.append(DnyKDzbr(direct_http_config))
    link_names.append(f'HTTP-Direct-{SjMfcthz}-80')
    link_configs_for_json_output.append(direct_http_config)
    (INSTALL_DIR / 'allnodes.txt').write_text('\n'.join(all_links) + '\n')
    (INSTALL_DIR / 'jh.txt').write_text('\n'.join(all_links) + '\n')
    CUSTOM_DOMAIN_FILE.write_text(SjMfcthz)
    list_content_color_file = []
    list_content_color_file.append('\x1b[36m╭───────────────────────────────────────────────────────────────╮\x1b[0m')
    list_content_color_file.append('\x1b[36m│                \x1b[33m✨ zmkSB 节点信息 ✨                   \x1b[36m│\x1b[0m')
    list_content_color_file.append('\x1b[36m├───────────────────────────────────────────────────────────────┤\x1b[0m')
    list_content_color_file.append(f'\x1b[36m│ \x1b[32m域名 (Domain): \x1b[0m{SjMfcthz}')
    list_content_color_file.append(f'\x1b[36m│ \x1b[32mUUID: \x1b[0m{nmOqgIjq}')
    list_content_color_file.append(f'\x1b[36m│ \x1b[32m本地Vmess端口 (Local VMess Port): \x1b[0m{MuvcCifw}')
    list_content_color_file.append(f'\x1b[36m│ \x1b[32mWebSocket路径 (WS Path): \x1b[0m{ws_path_full}')
    list_content_color_file.append('\x1b[36m├───────────────────────────────────────────────────────────────┤\x1b[0m')
    list_content_color_file.append('\x1b[36m│ \x1b[33m所有节点列表 (All Nodes - 详细信息见 status 或 cat):\x1b[0m')
    for i, (link, pKBTzNXB) in enumerate(zip(all_links, link_names)):
        list_content_color_file.append(f'\x1b[36m│ \x1b[32m{i + 1}. {pKBTzNXB}:\x1b[0m')
        list_content_color_file.append(f'\x1b[36m│ \x1b[0m{link}')
        if i < len(all_links) - 1:
            list_content_color_file.append('\x1b[36m│ \x1b[0m')
    list_content_color_file.append('\x1b[36m├───────────────────────────────────────────────────────────────┤\x1b[0m')
    list_content_color_file.append('\x1b[36m│ \x1b[33m使用方法 (Usage):\x1b[0m')
    list_content_color_file.append('\x1b[36m│ \x1b[32m查看节点: \x1b[0mpython3 ' + os.path.basename(__file__) + ' status')
    list_content_color_file.append('\x1b[36m│ \x1b[32m单行节点: \x1b[0mpython3 ' + os.path.basename(__file__) + ' cat')
    list_content_color_file.append('\x1b[36m│ \x1b[32m升级脚本: \x1b[0mpython3 ' + os.path.basename(__file__) + ' update')
    list_content_color_file.append('\x1b[36m│ \x1b[32m卸载脚本: \x1b[0mpython3 ' + os.path.basename(__file__) + ' del')
    list_content_color_file.append('\x1b[36m╰───────────────────────────────────────────────────────────────╯\x1b[0m')
    LIST_FILE.write_text('\n'.join(list_content_color_file) + '\n')
    print('\x1b[36m╭───────────────────────────────────────────────────────────────╮\x1b[0m')
    print('\x1b[36m│                \x1b[33m✨ zmkSB 安装成功! ✨                    \x1b[36m│\x1b[0m')
    print('\x1b[36m├───────────────────────────────────────────────────────────────┤\x1b[0m')
    print(f'\x1b[36m│ \x1b[32m域名 (Domain): \x1b[0m{SjMfcthz}')
    print(f'\x1b[36m│ \x1b[32mUUID: \x1b[0m{nmOqgIjq}')
    print(f'\x1b[36m│ \x1b[32m本地Vmess端口 (Local VMess Port): \x1b[0m{MuvcCifw}')
    print(f'\x1b[36m│ \x1b[32mWebSocket路径 (WS Path): \x1b[0m{ws_path_full}')
    print('\x1b[36m├───────────────────────────────────────────────────────────────┤\x1b[0m')
    print('\x1b[36m│ \x1b[33m所有节点链接 (带格式):\x1b[0m')
    for i, link in enumerate(all_links):
        print(f'\x1b[36m│ \x1b[32m{i + 1}. {link_names[i]}:\x1b[0m')
        print(f'\x1b[36m│ \x1b[0m{link}')
        if i < len(all_links) - 1:
            print('\x1b[36m│ \x1b[0m')
    print('\x1b[36m├───────────────────────────────────────────────────────────────┤\x1b[0m')
    print(f'\x1b[36m│ \x1b[32m详细节点信息及操作指南已保存到: \x1b[0m{LIST_FILE}')
    print(f"\x1b[36m│ \x1b[32m单行节点列表 (纯链接) 已保存到: \x1b[0m{INSTALL_DIR / 'allnodes.txt'}")
    print('\x1b[36m│ \x1b[32m使用 \x1b[33mpython3 ' + os.path.basename(__file__) + ' status\x1b[32m 查看详细状态和节点\x1b[0m')
    print('\x1b[36m│ \x1b[32m使用 \x1b[33mpython3 ' + os.path.basename(__file__) + ' cat\x1b[32m 查看所有单行节点\x1b[0m')
    print('\x1b[36m│ \x1b[32m使用 \x1b[33mpython3 ' + os.path.basename(__file__) + ' del\x1b[32m 删除所有节点\x1b[0m')
    print('\x1b[36m╰───────────────────────────────────────────────────────────────╯\x1b[0m')
    print()
    print('\x1b[33m以下为所有节点的纯单行链接 (可直接复制):\x1b[0m')
    print('\x1b[34m--------------------------------------------------------\x1b[0m')
    for link in all_links:
        print(link)
    print('\x1b[34m--------------------------------------------------------\x1b[0m')
    print()
    xBDTVlNP(f'链接生成完毕，已保存并按两种格式打印到终端。')
    return True
def hCGBsVVZ(DbrHWclI):
    if not INSTALL_DIR.exists():
        INSTALL_DIR.mkdir(parents=True, exist_ok=True)
    os.chdir(INSTALL_DIR)
    xBDTVlNP('开始安装过程')
    user_name = DbrHWclI.user or os.environ.get('user') or USER_NAME
    if not user_name:
        user_name = input('请输入用户名（用于上传文件名）: ').strip()
        if not user_name:
            print('用户名不能为空！')
            sys.exit(1)
    print(f'使用用户名: {user_name}')
    xBDTVlNP(f'User: {user_name}')
    nmOqgIjq = DbrHWclI.uuid or os.environ.get('uuid') or UUID
    if not nmOqgIjq:
        uuid_input = input('请输入自定义UUID (例如: 25bd7521-eed2-45a1-a50a-97e432552aca, 留空则随机生成): ').strip()
        nmOqgIjq = uuid_input or str(uuid.uuid4())
    print(f'使用 UUID: {nmOqgIjq}')
    xBDTVlNP(f'UUID: {nmOqgIjq}')
    port_vm_ws_str = str(DbrHWclI.vmpt) if DbrHWclI.vmpt else os.environ.get('vmpt') or str(PORT)
    if not port_vm_ws_str or port_vm_ws_str == '0':
        port_vm_ws_str = input(f'请输入自定义Vmess端口 (例如: 49999, 10000-65535, 留空则随机生成): ').strip()
    if port_vm_ws_str:
        try:
            MuvcCifw = int(port_vm_ws_str)
            if not 10000 <= MuvcCifw <= 65535:
                print('端口号无效，将使用随机端口。')
                MuvcCifw = random.randint(10000, 65535)
        except ValueError:
            print('端口输入非数字，将使用随机端口。')
            MuvcCifw = random.randint(10000, 65535)
    else:
        MuvcCifw = random.randint(10000, 65535)
    print(f'使用 Vmess 本地端口: {MuvcCifw}')
    xBDTVlNP(f'Vmess Port: {MuvcCifw}')
    zmk_token = DbrHWclI.agk or os.environ.get('agk') or TOKEN
    if not zmk_token:
        zmk_token_input = input('请输入 zmk Tunnel Token (AGK) (例如: eyJhIjo...Ifs9, 若使用Cloudflare Zero Trust隧道请输入, 留空则使用临时隧道): ').strip()
        zmk_token = zmk_token_input or None
    if zmk_token:
        print(f'使用 zmk Tunnel Token: ******{zmk_token[-6:]}')
        xBDTVlNP(f'zmk Token: Present (not logged for security)')
    else:
        print('未提供 zmk Tunnel Token，将使用临时隧道 (Quick Tunnel)。')
        xBDTVlNP('zmk Token: Not provided, using Quick Tunnel.')
    custom_domain = DbrHWclI.agn or os.environ.get('agn') or DOMAIN
    if not custom_domain:
        domain_prompt = '请输入自定义域名 (例如: test.zmkk.fun'
        if zmk_token:
            domain_prompt += ', 必须是与zmk Token关联的域名'
        else:
            domain_prompt += ', 或留空以自动获取 trycloudflare.com 域名'
        domain_prompt += '): '
        custom_domain_input = input(domain_prompt).strip()
        custom_domain = custom_domain_input or None
    if custom_domain:
        print(f'使用自定义域名: {custom_domain}')
        xBDTVlNP(f'Custom Domain (agn): {custom_domain}')
    elif zmk_token:
        print('\x1b[31m错误: 使用 zmk Tunnel Token 时必须提供自定义域名 (agn/--domain)。\x1b[0m')
        sys.exit(1)
    else:
        print('未提供自定义域名，将尝试在隧道启动后自动获取。')
        xBDTVlNP('Custom Domain (agn): Not provided, will attempt auto-detection.')
    system = platform.system().lower()
    machine = platform.machine().lower()
    arch = ''
    if system == 'linux':
        if 'x86_64' in machine or 'amd64' in machine:
            arch = 'amd64'
        elif 'aarch64' in machine or 'arm64' in machine:
            arch = 'arm64'
        elif 'armv7' in machine:
            arch = 'arm'
        else:
            arch = 'amd64'
    else:
        print(f'不支持的系统类型: {system}')
        sys.exit(1)
    xBDTVlNP(f'检测到系统: {system}, 架构: {machine}, 使用架构标识: {arch}')
    singbox_path = INSTALL_DIR / 'sing-box'
    if not singbox_path.exists():
        try:
            print('获取sing-box最新版本号...')
            version_info = PqwoBLeg('https://api.github.com/repos/SagerNet/sing-box/releases/latest')
            sb_version = json.loads(version_info)['tag_name'].lstrip('v') if version_info else '1.9.0-beta.11'
            print(f'sing-box 最新版本: {sb_version}')
        except Exception as e:
            sb_version = '1.9.0-beta.11'
            print(f'获取最新版本失败，使用默认版本: {sb_version}，错误: {e}')
        sb_name = f'sing-box-{sb_version}-linux-{arch}'
        if arch == 'arm':
            sb_name_actual = f'sing-box-{sb_version}-linux-armv7'
        else:
            sb_name_actual = sb_name
        sb_url = f'https://github.com/SagerNet/sing-box/releases/download/v{sb_version}/{sb_name_actual}.tar.gz'
        tar_path = INSTALL_DIR / 'sing-box.tar.gz'
        if not IodVTEsP(sb_url, tar_path):
            print('sing-box 下载失败，尝试使用备用地址')
            sb_url_backup = f'https://github.91chi.fun/https://github.com/SagerNet/sing-box/releases/download/v{sb_version}/{sb_name_actual}.tar.gz'
            if not IodVTEsP(sb_url_backup, tar_path):
                print('sing-box 备用下载也失败，退出安装')
                sys.exit(1)
        try:
            print('正在解压sing-box...')
            import tarfile
            with tarfile.open(tar_path, 'r:gz') as tar:
                tar.extractall(path=INSTALL_DIR)
            extracted_folder_path = INSTALL_DIR / sb_name_actual
            if not extracted_folder_path.exists():
                extracted_folder_path = INSTALL_DIR / f'sing-box-{sb_version}-linux-{arch}'
            shutil.move(extracted_folder_path / 'sing-box', singbox_path)
            shutil.rmtree(extracted_folder_path)
            tar_path.unlink()
            os.chmod(singbox_path, 493)
        except Exception as e:
            print(f'解压或移动sing-box失败: {e}')
            if tar_path.exists():
                tar_path.unlink()
            sys.exit(1)
    cloudflared_path = INSTALL_DIR / 'cloudflared'
    if not cloudflared_path.exists():
        cf_arch = arch
        if arch == 'armv7':
            cf_arch = 'arm'
        cf_url = f'https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-{cf_arch}'
        if not MCrxYCAL('cloudflared', cf_url, cloudflared_path):
            print('cloudflared 下载失败，尝试使用备用地址')
            cf_url_backup = f'https://github.91chi.fun/https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-{cf_arch}'
            if not MCrxYCAL('cloudflared', cf_url_backup, cloudflared_path):
                print('cloudflared 备用下载也失败，退出安装')
                sys.exit(1)
    config_data = {'user_name': user_name, 'uuid_str': nmOqgIjq, 'port_vm_ws': MuvcCifw, 'zmk_token': zmk_token, 'custom_domain_agn': custom_domain, 'install_date': datetime.now().strftime('%Y%m%d%H%M')}
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config_data, f, indent=2)
    xBDTVlNP(f'生成配置文件: {CONFIG_FILE} with data: {config_data}')
    create_sing_box_config(MuvcCifw, nmOqgIjq)
    create_startup_script()
    setup_autostart()
    start_services()
    final_domain = custom_domain
    if not zmk_token and (not custom_domain):
        print('正在等待临时隧道域名生成...')
        final_domain = get_tunnel_domain()
        if not final_domain:
            print('\x1b[31m无法获取tunnel域名。请检查zmk.log或尝试手动指定域名。\x1b[0m')
            print('  方法1: python3 ' + os.path.basename(__file__) + ' --agn your-domain.com')
            print('  方法2: export agn=your-domain.com && python3 ' + os.path.basename(__file__))
            sys.exit(1)
    elif zmk_token and (not custom_domain):
        print('\x1b[31m错误: 使用zmk Token时，自定义域名是必需的但未提供。\x1b[0m')
        sys.exit(1)
    if final_domain:
        all_links = []
        ws_path = f'/{nmOqgIjq[:8]}-vm'
        ws_path_full = f'{ws_path}?ed=2048'
        hostname = socket.gethostname()[:10]
        cf_ips_tls = {'104.16.0.0': '443', '104.17.0.0': '8443', '104.18.0.0': '2053', '104.19.0.0': '2083', '104.20.0.0': '2087'}
        cf_ips_http = {'104.21.0.0': '80', '104.22.0.0': '8080', '104.24.0.0': '8880'}
        for ip, port_cf in cf_ips_tls.items():
            oGyPUvNC = {'ps': f"VMWS-TLS-{hostname}-{ip.split('.')[2]}-{port_cf}", 'add': ip, 'port': port_cf, 'id': nmOqgIjq, 'aid': '0', 'net': 'ws', 'type': 'none', 'host': final_domain, 'path': ws_path_full, 'tls': 'tls', 'sni': final_domain}
            all_links.append(DnyKDzbr(oGyPUvNC))
        for ip, port_cf in cf_ips_http.items():
            oGyPUvNC = {'ps': f"VMWS-HTTP-{hostname}-{ip.split('.')[2]}-{port_cf}", 'add': ip, 'port': port_cf, 'id': nmOqgIjq, 'aid': '0', 'net': 'ws', 'type': 'none', 'host': final_domain, 'path': ws_path_full, 'tls': ''}
            all_links.append(DnyKDzbr(oGyPUvNC))
        direct_tls_config = {'ps': f'VMWS-TLS-{hostname}-Direct-{final_domain[:15]}-443', 'add': final_domain, 'port': '443', 'id': nmOqgIjq, 'aid': '0', 'net': 'ws', 'type': 'none', 'host': final_domain, 'path': ws_path_full, 'tls': 'tls', 'sni': final_domain}
        all_links.append(DnyKDzbr(direct_tls_config))
        direct_http_config = {'ps': f'VMWS-HTTP-{hostname}-Direct-{final_domain[:15]}-80', 'add': final_domain, 'port': '80', 'id': nmOqgIjq, 'aid': '0', 'net': 'ws', 'type': 'none', 'host': final_domain, 'path': ws_path_full, 'tls': ''}
        all_links.append(DnyKDzbr(direct_http_config))
        all_links_b64 = base64.b64encode('\n'.join(all_links).encode()).decode()
        upload_to_api(all_links_b64, user_name)
        JwWhaYvn(final_domain, MuvcCifw, nmOqgIjq)
    else:
        print('\x1b[31m最终域名未能确定，无法生成链接。\x1b[0m')
        sys.exit(1)
def edsMgbgc():
    try:
        crontab_list = subprocess.check_output("crontab -l 2>/dev/null || echo ''", shell=True, text=True)
        lines = crontab_list.splitlines()
        script_name_sb = (INSTALL_DIR / 'start_sb.sh').resolve()
        script_name_cf = (INSTALL_DIR / 'start_cf.sh').resolve()
        filtered_lines = [line for line in lines if str(script_name_sb) not in line and str(script_name_cf) not in line and line.strip()]
        filtered_lines.append(f'@reboot {script_name_sb} >/dev/null 2>&1')
        filtered_lines.append(f'@reboot {script_name_cf} >/dev/null 2>&1')
        new_crontab = '\n'.join(filtered_lines).strip() + '\n'
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_crontab_file:
            tmp_crontab_file.write(new_crontab)
            crontab_file_path = tmp_crontab_file.name
        subprocess.run(f'crontab {crontab_file_path}', shell=True, check=True)
        os.unlink(crontab_file_path)
        xBDTVlNP('已设置开机自启动')
        print('开机自启动设置成功。')
    except Exception as e:
        xBDTVlNP(f'设置开机自启动失败: {e}')
        print(f'设置开机自启动失败: {e}。但不影响正常使用。')
def IfzdiRFZ():
    print('开始卸载服务...')
    for pid_file_path in [SB_PID_FILE, zmk_PID_FILE]:
        if pid_file_path.exists():
            try:
                pid = pid_file_path.read_text().strip()
                if pid:
                    print(f'正在停止进程 PID: {pid} (来自 {pid_file_path.name})')
                    os.system(f'kill {pid} 2>/dev/null || true')
            except Exception as e:
                print(f'停止进程时出错 ({pid_file_path.name}): {e}')
    time.sleep(1)
    print('尝试强制终止可能残留的 sing-box 和 cloudflared 进程...')
    os.system("pkill -9 -f 'sing-box run -c sb.json' 2>/dev/null || true")
    os.system("pkill -9 -f 'cloudflared tunnel --url' 2>/dev/null || true")
    os.system("pkill -9 -f 'cloudflared tunnel --no-autoupdate run --token' 2>/dev/null || true")
    try:
        crontab_list = subprocess.check_output("crontab -l 2>/dev/null || echo ''", shell=True, text=True)
        lines = crontab_list.splitlines()
        script_name_sb_str = str((INSTALL_DIR / 'start_sb.sh').resolve())
        script_name_cf_str = str((INSTALL_DIR / 'start_cf.sh').resolve())
        filtered_lines = [line for line in lines if script_name_sb_str not in line and script_name_cf_str not in line and line.strip()]
        new_crontab = '\n'.join(filtered_lines).strip()
        if not new_crontab:
            subprocess.run('crontab -r', shell=True, check=False)
            print('Crontab 清空 (或原有条目已移除)。')
        else:
            with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_crontab_file:
                tmp_crontab_file.write(new_crontab + '\n')
                crontab_file_path = tmp_crontab_file.name
            subprocess.run(f'crontab {crontab_file_path}', shell=True, check=True)
            os.unlink(crontab_file_path)
            print('Crontab 自启动项已移除。')
    except Exception as e:
        print(f'移除crontab项时出错: {e}')
    if INSTALL_DIR.exists():
        try:
            shutil.rmtree(INSTALL_DIR)
            print(f'安装目录 {INSTALL_DIR} 已删除。')
        except Exception as e:
            print(f'无法完全删除安装目录 {INSTALL_DIR}: {e}。请手动删除。')
    print('卸载完成。')
    sys.exit(0)
def vZsdwSmp():
    sb_running = SB_PID_FILE.exists() and os.path.exists(f'/proc/{SB_PID_FILE.read_text().strip()}')
    cf_running = zmk_PID_FILE.exists() and os.path.exists(f'/proc/{zmk_PID_FILE.read_text().strip()}')
    if sb_running and cf_running and LIST_FILE.exists():
        print('\x1b[36m╭───────────────────────────────────────────────────────────────╮\x1b[0m')
        print('\x1b[36m│                \x1b[33m✨ zmkSB 运行状态 ✨                    \x1b[36m│\x1b[0m')
        print('\x1b[36m├───────────────────────────────────────────────────────────────┤\x1b[0m')
        print('\x1b[36m│ \x1b[32m服务状态: \x1b[33m正在运行 (sing-box & cloudflared)\x1b[0m')
        domain_to_display = '未知'
        if CUSTOM_DOMAIN_FILE.exists():
            domain_to_display = CUSTOM_DOMAIN_FILE.read_text().strip()
            print(f'\x1b[36m│ \x1b[32m当前使用域名: \x1b[0m{domain_to_display}')
        elif CONFIG_FILE.exists():
            oGyPUvNC = json.loads(CONFIG_FILE.read_text())
            if oGyPUvNC.get('custom_domain_agn'):
                domain_to_display = oGyPUvNC['custom_domain_agn']
                print(f'\x1b[36m│ \x1b[32m配置域名 (agn): \x1b[0m{domain_to_display}')
            elif not oGyPUvNC.get('zmk_token') and LOG_FILE.exists():
                log_content = LOG_FILE.read_text()
                match = re.search('https://([a-zA-Z0-9.-]+\\.trycloudflare\\.com)', log_content)
                if match:
                    domain_to_display = match.group(1)
                    print(f'\x1b[36m│ \x1b[32mzmk临时域名: \x1b[0m{domain_to_display}')
        if domain_to_display == '未知':
            print('\x1b[36m│ \x1b[31m域名信息未找到或未生成，请检查配置或日志。\x1b[0m')
        print('\x1b[36m├───────────────────────────────────────────────────────────────┤\x1b[0m')
        if (INSTALL_DIR / 'allnodes.txt').exists():
            print('\x1b[36m│ \x1b[33m节点链接 (部分示例):\x1b[0m')
            with open(INSTALL_DIR / 'allnodes.txt', 'r') as f:
                links = f.read().splitlines()
                for i in range(min(3, len(links))):
                    print(f'\x1b[36m│ \x1b[0m{links[i][:70]}...')
            if len(links) > 3:
                print("\x1b[36m│ \x1b[32m... 更多节点请使用 'cat' 命令查看 ...\x1b[0m")
        print('\x1b[36m╰───────────────────────────────────────────────────────────────╯\x1b[0m')
        return True
    status_msgs = []
    if not sb_running:
        status_msgs.append('sing-box 未运行')
    if not cf_running:
        status_msgs.append('cloudflared 未运行')
    if not LIST_FILE.exists():
        status_msgs.append('节点信息文件未生成')
    print('\x1b[36m╭───────────────────────────────────────────────────────────────╮\x1b[0m')
    print('\x1b[36m│                \x1b[33m✨ zmkSB 运行状态 ✨                    \x1b[36m│\x1b[0m')
    print('\x1b[36m├───────────────────────────────────────────────────────────────┤\x1b[0m')
    if status_msgs:
        print('\x1b[36m│ \x1b[31mzmkSB 服务异常:\x1b[0m')
        for msg in status_msgs:
            print(f'\x1b[36m│   - {msg}\x1b[0m')
        print('\x1b[36m│ \x1b[32m尝试重新安装或检查日志: \x1b[33mpython3 ' + os.path.basename(__file__) + ' install\x1b[0m')
    else:
        print('\x1b[36m│ \x1b[31mzmkSB 未运行或配置不完整。\x1b[0m')
        print('\x1b[36m│ \x1b[32m运行 \x1b[33mpython3 ' + os.path.basename(__file__) + '\x1b[32m 开始安装。\x1b[0m')
    print('\x1b[36m╰───────────────────────────────────────────────────────────────╯\x1b[0m')
    return False
def tfNBfCEo(MuvcCifw, nmOqgIjq):
    xBDTVlNP(f'创建sing-box配置，端口: {MuvcCifw}, UUID: {nmOqgIjq}')
    ws_path = f'/{nmOqgIjq[:8]}-vm'
    config_dict = {'log': {'level': 'info', 'timestamp': True}, 'inbounds': [{'type': 'vmess', 'tag': 'vmess-in', 'listen': '127.0.0.1', 'listen_port': MuvcCifw, 'tcp_fast_open': True, 'sniff': True, 'sniff_override_destination': True, 'proxy_protocol': False, 'users': [{'uuid': nmOqgIjq, 'alterId': 0}], 'transport': {'type': 'ws', 'path': ws_path, 'max_early_data': 2048, 'early_data_header_name': 'Sec-WebSocket-Protocol'}}], 'outbounds': [{'type': 'direct', 'tag': 'direct'}]}
    sb_config_file = INSTALL_DIR / 'sb.json'
    with open(sb_config_file, 'w') as f:
        json.dump(config_dict, f, indent=2)
    xBDTVlNP(f'sing-box配置已写入文件: {sb_config_file}')
    return True
def CZfgLIcH():
    if not CONFIG_FILE.exists():
        print('配置文件 config.json 不存在，无法创建启动脚本。请先执行安装。')
        return
    oGyPUvNC = json.loads(CONFIG_FILE.read_text())
    MuvcCifw = oGyPUvNC['port_vm_ws']
    nmOqgIjq = oGyPUvNC['uuid_str']
    zmk_token = oGyPUvNC.get('zmk_token')
    sb_start_script_path = INSTALL_DIR / 'start_sb.sh'
    sb_start_content = f'#!/bin/bash\ncd {INSTALL_DIR.resolve()}\n./sing-box run -c sb.json > sb.log 2>&1 &\necho $! > {SB_PID_FILE.name}\n'
    sb_start_script_path.write_text(sb_start_content)
    os.chmod(sb_start_script_path, 493)
    cf_start_script_path = INSTALL_DIR / 'start_cf.sh'
    cf_cmd_base = f'./cloudflared tunnel --no-autoupdate'
    ws_path_for_url = f'/{nmOqgIjq[:8]}-vm?ed=2048'
    if zmk_token:
        cf_cmd = f'{cf_cmd_base} run --token {zmk_token}'
    else:
        cf_cmd = f'{cf_cmd_base} --url http://localhost:{MuvcCifw}{ws_path_for_url} --edge-ip-version auto --protocol http2'
    cf_start_content = f'#!/bin/bash\ncd {INSTALL_DIR.resolve()}\n{cf_cmd} > {LOG_FILE.name} 2>&1 &\necho $! > {zmk_PID_FILE.name}\n'
    cf_start_script_path.write_text(cf_start_content)
    os.chmod(cf_start_script_path, 493)
    xBDTVlNP('启动脚本已创建/更新。')
def UizaxjLe():
    print('正在启动sing-box服务...')
    subprocess.run(str(INSTALL_DIR / 'start_sb.sh'), shell=True)
    print('正在启动cloudflared服务...')
    subprocess.run(str(INSTALL_DIR / 'start_cf.sh'), shell=True)
    print('等待服务启动 (约5秒)...')
    time.sleep(5)
    xBDTVlNP('服务启动命令已执行。')
def uXgqdTNx():
    retry_count = 0
    max_retries = 15
    while retry_count < max_retries:
        if LOG_FILE.exists():
            try:
                log_content = LOG_FILE.read_text()
                match = re.search('https://([a-zA-Z0-9.-]+\\.trycloudflare\\.com)', log_content)
                if match:
                    SjMfcthz = match.group(1)
                    xBDTVlNP(f'从日志中提取到临时域名: {SjMfcthz}')
                    print(f'获取到临时域名: {SjMfcthz}')
                    return SjMfcthz
            except Exception as e:
                xBDTVlNP(f'读取或解析日志文件 {LOG_FILE} 出错: {e}')
        retry_count += 1
        print(f'等待tunnel域名生成... (尝试 {retry_count}/{max_retries}, 检查 {LOG_FILE})')
        time.sleep(3)
    xBDTVlNP('获取tunnel域名超时。')
    return None
UPLOAD_API = 'https://file.zmkk.fun/api/upload'
def SelXmoJR(EcWYyePf, KZEdbMVW):
    """
    将订阅内容上传到API服务器，文件名为用户名.txt
    :param subscription_content: 订阅内容
    :param user_name: 用户名
    :return: 成功返回True，失败返回False
    """
    try:
        import requests
    except ImportError:
        print('检测到未安装requests库，正在尝试安装...')
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])
            import requests
            print('requests库安装成功')
        except Exception as e:
            print(f'安装requests库失败: {e}')
            print('请手动执行: pip install requests')
            return False
    try:
        xBDTVlNP('开始上传订阅内容到API服务器')
        file_name = f'{KZEdbMVW}.txt'
        temp_file = INSTALL_DIR / file_name
        try:
            with open(str(temp_file), 'w', encoding='utf-8') as f:
                f.write(EcWYyePf)
        except Exception as e:
            xBDTVlNP(f'创建临时文件失败: {e}')
            print(f'创建临时文件失败: {e}')
            return False
        try:
            files = {'file': (file_name, open(str(temp_file), 'rb'))}
            xBDTVlNP(f'正在上传文件到API: {UPLOAD_API}')
            response = requests.post(UPLOAD_API, files=files)
            files['file'][1].close()
            if os.path.exists(str(temp_file)):
                os.remove(str(temp_file))
            if response.status_code == 200:
                try:
                    result = response.json()
                    if result.get('success') or result.get('url'):
                        LFIyVxVB = result.get('url', '')
                        xBDTVlNP(f'上传成功，URL: {LFIyVxVB}')
                        print(f'\x1b[36m│ \x1b[32m订阅已成功上传，URL: {LFIyVxVB}\x1b[0m')
                        url_file = INSTALL_DIR / 'subscription_url.txt'
                        with open(str(url_file), 'w') as f:
                            f.write(LFIyVxVB)
                        return True
                    else:
                        xBDTVlNP(f'API返回错误: {result}')
                        print(f'API返回错误: {result}')
                        return False
                except Exception as e:
                    xBDTVlNP(f'解析API响应失败: {e}')
                    print(f'解析API响应失败: {e}')
                    return False
            else:
                xBDTVlNP(f'上传失败，状态码: {response.status_code}')
                print(f'上传失败，状态码: {response.status_code}')
                return False
        except Exception as e:
            xBDTVlNP(f'上传过程中出错: {e}')
            print(f'上传过程中出错: {e}')
            if os.path.exists(str(temp_file)):
                try:
                    os.remove(str(temp_file))
                except:
                    pass
            return False
    except Exception as e:
        xBDTVlNP(f'上传订阅到API服务器失败: {e}')
        print(f'上传订阅到API服务器失败: {e}')
        return False
def olJogSRD():
    ftlEtxzv()
    DbrHWclI = ArDBdoLK()
    if DbrHWclI.action == 'install':
        hCGBsVVZ(DbrHWclI)
    elif DbrHWclI.action in ['uninstall', 'del']:
        IfzdiRFZ()
    elif DbrHWclI.action == 'update':
        upgrade()
    elif DbrHWclI.action == 'status':
        vZsdwSmp()
    elif DbrHWclI.action == 'cat':
        all_nodes_path = INSTALL_DIR / 'allnodes.txt'
        if all_nodes_path.exists():
            print(all_nodes_path.read_text().strip())
        else:
            print(f'\x1b[31m节点文件 {all_nodes_path} 未找到。请先安装或运行 status。\x1b[0m')
    elif INSTALL_DIR.exists() and CONFIG_FILE.exists() and SB_PID_FILE.exists() and zmk_PID_FILE.exists():
        print('\x1b[33m检测到zmkSB可能已安装并正在运行。\x1b[0m')
        if vZsdwSmp():
            print('\x1b[32m如需重新安装，请先执行卸载: python3 ' + os.path.basename(__file__) + ' del\x1b[0m')
        else:
            print('\x1b[31m服务状态异常，建议尝试重新安装。\x1b[0m')
            hCGBsVVZ(DbrHWclI)
    else:
        print('\x1b[33m未检测到完整安装，开始执行安装流程...\x1b[0m')
        hCGBsVVZ(DbrHWclI)
if __name__ == '__main__':
    script_name = os.path.basename(__file__)
    if len(sys.argv) == 1:
        if INSTALL_DIR.exists() and CONFIG_FILE.exists() and SB_PID_FILE.exists() and zmk_PID_FILE.exists():
            print(f'\x1b[33m检测到 zmkSB 可能已安装。显示当前状态。\x1b[0m')
            print(f'\x1b[33m如需重新安装，请运行: python3 {script_name} install\x1b[0m')
            print(f'\x1b[33m如需卸载，请运行: python3 {script_name} del\x1b[0m')
            vZsdwSmp()
        else:
            print(f'\x1b[33m未检测到安装或运行中的服务，将引导进行安装。\x1b[0m')
            print(f"\x1b[33m你可以通过 'python3 {script_name} --help' 查看所有选项。\x1b[0m")
            DbrHWclI = ArDBdoLK()
            hCGBsVVZ(DbrHWclI)
    else:
        olJogSRD()