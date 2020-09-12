Public MustInherit Class Singleton(Of T As New)

    ' Singleton
    Public Sub New()

    End Sub

    Public Shared ReadOnly Property GetInstance As T
        Get
            Static Instance As T = New T()
            Return Instance
        End Get
    End Property
    ' Singleton
End Class
