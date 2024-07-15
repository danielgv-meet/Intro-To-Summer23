def create_youtube_video(title, description):
	video_dict = {"title": title, "description": description, "likes": 0, "dislikes": 0, "comments": {}, "hashtag":[]}
	print("Enter five words that describe your video: ")
	for time in range(5):
		word = input()
		video_dict["hashtag"].append(word)
	return video_dict


def like(video_dict):
	if "likes" in video_dict:
		video_dict["likes"] += 1
	return video_dict


def dislike(video_dict):
	if "dislikes" in video_dict:
		video_dict["dislikes"] += 1
	return video_dict


def add_comment(video_dict, username, comment_text):
	video_dict["comments"][username] = comment_text

	return video_dict


def similarity_to_video(first_video, second_video):
	similarity_counter = 0
	for word in first_video["hashtag"]:
		if word in second_video["hashtag"]:
				similarity_counter += 1
	print("The similarity between the videos is: " + str(similarity_counter * 20) + "%")


def main():
	title = input("Enter video title: ")
	description = input("Enter discription for the video: ")
	video_dict = create_youtube_video(title, description)
	users_choice = '0'
	for time in range(495):
		video_dict = like(video_dict)

	video_dict = dislike(video_dict)

	username = input("Enter your username: ")
	comment = input("Enter you comment text: ")
	video_dict = add_comment(video_dict, username, comment)

	print(video_dict)

	second_title = input("Enter the second video title: ")
	second_description = input("Enter second video discription: ")
	second_video_dict = create_youtube_video(second_title, second_description)
	print(second_video_dict)
	similarity_to_video(video_dict, second_video_dict)



if __name__ == "__main__":
	main()