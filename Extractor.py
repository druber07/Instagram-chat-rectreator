import json,io

def get_Date(date):
	date = date.split('T')
	return date[0]

def save_file(index, data):
	info = []
	arrang = 0
	for n in data[index]["conversation"]:
		if 'story_share' in n.keys():
			if n["text"] == None:
				info.append(n["sender"]+"+"+n["story_share"]+"+"+get_Date(n["created_at"])+"∫")
				print(n["sender"],"/",n["story_share"],"/",get_Date(n["created_at"]))
			else:
				info.append(n["sender"]+"+"+n["text"]+', '+n["story_share"]+"+"+get_Date(n["created_at"])+"∫")
				print(n["sender"],"/",n["text"],"/",n["story_share"],"/",get_Date(n["created_at"]))
		elif 'text' in n.keys():
			info.append(n["sender"]+"+"+n["text"]+"+"+get_Date(n["created_at"])+"∫")
			print(n["sender"],"/",n["text"],"/",get_Date(n["created_at"]))
		elif 'media' in n.keys():
			info.append(n["sender"]+"+"+n["media"]+"+"+get_Date(n["created_at"])+"∫")		
			print(n["sender"],"/",n["media"],"/",get_Date(n["created_at"]))
		elif 'media_share_caption' in n.keys():
			info.append(n["sender"]+"+"+n["media_share_url"]+"+"+get_Date(n["created_at"])+"∫")
			print(n["sender"],"/",n["media_share_caption"],"/",n["media_share_url"],"/",get_Date(n["created_at"]))
		elif 'voice_media' in n.keys():
			info.append(n["sender"]+"+"+'Audio message'+"+"+get_Date(n["created_at"])+"∫")
			print(n["sender"]+"+"+'Audio message'+"+"+get_Date(n["created_at"]))
		elif 'video_call_action' in n.keys():
			info.append(n["sender"]+"+"+'Video call'+"+"+get_Date(n["created_at"])+"∫")
			print(n["sender"]+"+"+'Video call'+"+"+get_Date(n["created_at"]))
		else:
			print(n.keys())
			info.append("Unkown+"+n["created_at"]+'+'+"∫")
			print(n.keys(),"/",n["created_at"])

	dataFile = open("./site/data.txt","w",encoding="utf-8")

	for x in info[::-1]:
		dataFile.write(x)

	print('Extracting was done successfully')

def get_index(name, data):
	n = 0
	for conversation in data:
		if conversation['participants'][0] == name or conversation['participants'][1] == name:
			print('User was found', n)
			return n
		n+=1
	print('Task failed, user was not found')
	return(-1)	

if __name__ == "__main__":
	name = input('Enter username\n')

	with open("messages.json", encoding="utf-8") as f:
		content = f.readlines()
	content = [x.strip() for x in content]
	data = json.loads(content[0])
	index = get_index(name, data)
	if(index != -1):
		save_file(index, data)