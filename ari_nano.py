import ari

# ARI connection details
ARI_URL = 'http://192.168.30.53:8088/'
ARI_USERNAME = 'asterisk'
ARI_PASSWORD = '@Botirjon06'

client = ari.connect(ARI_URL, ARI_USERNAME, ARI_PASSWORD)


def on_stasis_start(event, channel):
    print(f"Channel {channel.json.get('name')} entered Stasis app")
    # Extract and log relevant information
    caller = channel.json.get('caller', {}).get('number')
    called = channel.json.get('connected', {}).get('number')
    print(f"Caller: {caller}, Called: {called}")


def on_dial(event):
    print(f"Dial event: {event}")
    # You can extract more detailed information about the call here


def on_bridge_enter(event):
    print(f"Channel {event['channel']['id']} entered bridge {event['bridge']['id']}")
    # You can log information about participants in the bridge


client.on_channel_event('StasisStart', on_stasis_start)
client.on_event('Dial', on_dial)
client.on_event('BridgeEnter', on_bridge_enter)

client.run(apps='your_stasis_app')
