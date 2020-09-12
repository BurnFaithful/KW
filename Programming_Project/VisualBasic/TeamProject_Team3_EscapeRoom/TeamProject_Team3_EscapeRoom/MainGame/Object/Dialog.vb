Public Class Dialog

    Private id As Integer
    Public Property pId As Integer
        Get
            Return id
        End Get
        Set(value As Integer)
            id = value
        End Set
    End Property
    Private normalText As String
    Public Property pNormalTExt As String
        Get
            Return normalText
        End Get
        Set(value As String)
            normalText = value
        End Set
    End Property
    Private clearText As String
    Public Property pClearText As String
        Get
            Return clearText
        End Get
        Set(value As String)
            clearText = value
        End Set
    End Property

End Class
