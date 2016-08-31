import json
from watson_developer_cloud import ToneAnalyzerV3


tone_analyzer = ToneAnalyzerV3(
   username='1da2a265-4790-4b5d-8b3a-fe60c599a174',
   password='oTQyUwyqxrTh',
   version='2016-05-19 ')
print(json.dumps(tone_analyzer.tone(text='''You are now connected to Customer Service.
Customer: Hello.
Agent: Hello.
Agent: How can I help you today?
Customer: Someone created an account using my email account.
Customer: This is not my account.
Customer: How can I delete this account?
Agent: Okay, let me check this out for you.
Agent: One moment please.
Customer: Okay.
Customer: ?
Agent: Yeah.
Agent: Im here.
Agent: Im so sorry for taking a long time on this.
Agent: Okay, Ill reset your password.
Agent: Just check the link on it, so you can have your new password.
Customer: No.
Customer: I dont need you to reset my password.
Agent: Oh okay.
Agent: Sorry about that.
Customer: I need you to delete this fake account because it is not mine.
Customer: Please dont change my password.
Agent: Ah okay, yeah sure.
Agent: Im not going to change your password maam.
Customer: Maam?
Customer: What is going on here?
Agent: Oh so sorry to call you Ma\'am.
Agent: It\'s okay.
Agent: I got misinformation in here, but let me handle this for you.
Customer: Can you delete the fake account or not?
Agent: Okay.
Agent: Please give me another moment again.
Agent: Okay?
Customer: Okay.
Customer: Do you understand the problem I am having or is this a lost cause?
Customer: Can you please just let me know if this is a problem you can help resolve?
Agent: I recommend that you delete the e-mail.
Agent: For your protection, do not respond to it, and do not open any attachments or click any links it contains okay?
Customer: Delete my email?
Customer: Did you say delete my email?
Customer: Hello?
Customer: ?????
Agent: One moment please let me check on this for you.
Customer: One moment?!
Customer: Not sure what your definition of a moment is but this has been going on for a long time and you obviously have no idea what you are doing!
Customer: This is ridiculous!
Customer: You can\'t spell.
Customer: You aren\'t listening to my problem.
Customer: You keep asking me to wait a moment.
Customer: Ten minutes each time.
Customer: You suggest that I delete my email account, how the hell does that help?
Customer: You are very unhelpful.
Customer: I will ask one last time.
Customer: Can you delete this account or not?
Customer: Simple question.
Agent: Okay, I will refer you to our account specialist so this account gets deleted okay?
Customer: Read what you just typed.
Customer: It doesn\'t make sense.
Agent: I am really so sorry about this inconvenience but our account specialist will handle this for you okay?
Customer: Yes please put me in touch with someone.
Customer: ANYONE.
Agent: Okay, I will refer you to our account specialist so this account gets deleted okay?
Agent: That was a mistake so sorry about that.
Customer: Okay.
Customer: Please connect me with an account specialist.
Agent: I do apologize that this is taking longer than usual, however, let me go ahead right now and look for another available rep to call you.
Agent: Thank you for your patience and understanding!
'''), indent=2))
