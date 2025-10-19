import requests
import json

username = 'La_quecu'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://stripchat.com/',
    'Origin': 'https://stripchat.com'
}

print(f'Testing API for username: {username}')
print('-' * 50)

try:
    response = requests.get(f'https://stripchat.com/api/front/v2/models/username/{username}/cam', headers=headers, timeout=10)
    print(f'Status Code: {response.status_code}')
    print(f'Response Headers: {dict(response.headers)}')
    print('-' * 50)

    if response.status_code == 200:
        data = response.json()
        print(f'Full Response JSON:')
        print(json.dumps(data, indent=2))
        print('-' * 50)

        if 'cam' in data:
            cam = data['cam']
            print(f'\nCam Info:')
            print(f'  isCamAvailable: {cam.get("isCamAvailable")}')
            print(f'  streamName: {cam.get("streamName")}')
            print(f'  viewServers: {cam.get("viewServers")}')

            if 'viewServers' in cam and 'flashphoner-hls' in cam['viewServers']:
                hls_url = f'https://b-{cam["viewServers"]["flashphoner-hls"]}.doppiocdn.com/hls/{cam["streamName"]}/{cam["streamName"]}.m3u8'
                print(f'\n  Generated HLS URL: {hls_url}')
            else:
                print('\n  flashphoner-hls not found in viewServers')
        else:
            print('\n"cam" key not found in response')
    else:
        print(f'Error response: {response.text[:500]}')

except Exception as e:
    print(f'Exception: {type(e).__name__}: {e}')
