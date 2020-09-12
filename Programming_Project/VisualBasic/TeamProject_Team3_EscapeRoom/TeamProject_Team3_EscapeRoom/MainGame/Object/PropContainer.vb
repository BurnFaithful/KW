Public Class PropContainer
    Inherits Singleton(Of PropContainer)

    Private propList As New List(Of Prop)
    Public ReadOnly Property pPropList As List(Of Prop)
        Get
            Return propList
        End Get
    End Property

    Public Sub AddProp(parent As Control, pos As Point, _id As Integer)
        propList.Add(New Prop())
        propList.Last().Init(parent, pos, _id)
    End Sub ' Transparency + Definite Pos + Event Id set-up Prop

    Public Function GetProp(_id As Integer) As Prop
        For i = 0 To propList.Count - 1
            If propList.Item(i).pId = _id Then
                Return propList.Item(i)
            End If
        Next

        Return Nothing
    End Function

    Public Function GetProp(_pb As PictureBox) As Prop
        For i = 0 To propList.Count - 1
            If propList.Item(i).pPb.Name Like _pb.Name Then
                Return propList.Item(i)
            End If
        Next

        Return Nothing
    End Function

    Public Sub RemoveProp(_prop As Prop)
        propList.Remove(_prop)
    End Sub
End Class
