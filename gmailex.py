from gmail import GMail
from gmail import Message
from random import choice
list_reason = ['Đau bụng', 'Đau tay', 'Đau chân', 'Đau đầu', 'Đau mắt']
gmail = GMail('thanhdz0504@gmail.com', 'tienthanh')
html_content = """<p style="text-align: center;">Đơn xin nghỉ học</p>
<p style="text-align: left;">&nbsp;Em ch&agrave;o thầy,</p>
<p style="text-align: left;">&nbsp;T&ecirc;n em l&agrave; Nguyễn Tiến Th&agrave;nh</p>
<p style="text-align: left;">&nbsp;Mai {{sickness}} em xin ph&eacute;p nghỉ cả tuần ạ&nbsp;<img src="http://htmleditor.tools/tinymce465/plugins/emoticons/img/smiley-cry.gif" alt="cry" /></p>
<p style="text-align: left;">H&agrave; Nội, 18/3/2018&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;K&yacute; T&ecirc;n: Th&agrave;nh</p>
"""
new_mess = html_content.replace('{{sickness}}', choice(list_reason))
mess = Message('Subject', to='techkidsc4e16@gmail.com', html=new_mess)
gmail.send(mess)
