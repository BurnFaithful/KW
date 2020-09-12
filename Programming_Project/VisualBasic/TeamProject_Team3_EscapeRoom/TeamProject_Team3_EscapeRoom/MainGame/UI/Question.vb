Public Class Question

    Private id As Integer
    Public Property pId As Integer
        Get
            Return id
        End Get
        Set(value As Integer)
            id = value
        End Set
    End Property

    Private questionText As String
    Public Property pQuestionText
        Get
            Return questionText
        End Get
        Set(value)
            questionText = value
        End Set
    End Property

    Private questionAnswer As String
    Public Property pQuestionAnswer
        Get
            Return questionAnswer
        End Get
        Set(value)
            questionAnswer = value
        End Set
    End Property

End Class
