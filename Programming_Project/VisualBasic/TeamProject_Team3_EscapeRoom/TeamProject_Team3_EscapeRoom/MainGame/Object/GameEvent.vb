Public Class GameEvent

    Private id As Integer
    Public Property pId As Integer
        Get
            Return id
        End Get
        Set(value As Integer)
            id = value
        End Set
    End Property
    Private nextId As Integer
    Public Property pNextId As Integer
        Get
            Return nextId
        End Get
        Set(value As Integer)
            nextId = value
        End Set
    End Property

    Public Sub Init(_id As Integer, _nextId As Integer)
        id = _id
        nextId = _nextId
    End Sub
End Class
