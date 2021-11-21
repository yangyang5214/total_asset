# -*- coding: UTF-8 -*-
import logging

import requests

token_file = '/opt/qieman_token'


def get_asset_summary():
    try:
        with open(token_file, 'r') as f:
            qieman_token = f.readline().strip()
    except:
        pass
    finally:
        if not qieman_token:
            logging.error("read qieman_token error")
            return -1
    headers = {
        'Authorization': f'Bearer {qieman_token}',
        'x-sign': '1637468881280E80B4BDD476B79F05C29BF7BABBFB040',
        'User-Agent': 'qieman-ios/cn.yingmi.qieman-ios (198; iOS 15.1.0; iPhone12,1#iPhone 11) QiemaniOS/4.7.22/198',
    }

    response = requests.get('https://api.qieman.com/pmdj/v2/asset/summary', headers=headers, verify=False)
    if response.status_code == 200:
        return response.json().get('totalAsset', -1)
    return -1


if __name__ == '__main__':
    print(get_asset_summary())
