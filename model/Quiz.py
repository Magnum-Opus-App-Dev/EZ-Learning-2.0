class Quiz:
  def __init__(self, quiz_id, q_topic_id, type, question, answer, choices):

    self.quiz_id = quiz_id
    self.q_topic_id = q_topic_id
    self.type = type
    self.question = question
    self.answer = answer
    self.choices = choices