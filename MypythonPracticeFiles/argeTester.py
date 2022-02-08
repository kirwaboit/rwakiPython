import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--serverNumber', type=int, required=True)
parser.add_argument('--serverName', type=str)
args = parser.parse_args()
if args.serverName:
  print(args.serverNumber, 'is the server number and ', args.serverName, 'is the servername.')
else:
  print('Starting server No. ,', args.serverNumber , ' Refresh server stats to see status')