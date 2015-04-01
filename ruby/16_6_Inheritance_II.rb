#
class Message
    @@messages_sent = 0
    def initialize(from, to)
        @from = from
        @to = to
        @@messages_sent += 1
    end
end

class Email < Message
    def initialize(from, to, subject)
        super(from, to)
        @subject = subject
    end
end

my_message = Email.new("Diego", "Mona", "Asunto del mensaje")

