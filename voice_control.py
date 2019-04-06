import speech_recognition as sr
#sudo pip install SpeechRecognition
#sudo apt-get install portaudio19-dev python-all-dev python3-all-dev && 
#sudo pip install pyaudio
#use lsusb for usb microphone
class Voice:
	@staticmethod
	def get_voice_input():
		mic_name = None

		sample_rate = 48000
		chunk_size = 2048
		r = sr.Recognizer()
		mic_list = sr.Microphone.list_microphone_names()

		for i, microphone_name in enumerate(mic_list):
			#if microphone_name == mic_name:
			device_id = i  

		with sr.Microphone(device_index = device_id, sample_rate = sample_rate, 
								chunk_size = chunk_size) as source:


			r.adjust_for_ambient_noise(source)
			print ("Say Something")
			audio = r.listen(source)

			try: 
				text = r.recognize_google(audio)
				print(text)
				return (text)
	
			except sr.UnknownValueError: 
				print("Google Speech Recognition could not understand audio") 
	
			except sr.RequestError as e: 
				print("Could not request results from Google Speech Recognition service; {0}".format(e)) 

