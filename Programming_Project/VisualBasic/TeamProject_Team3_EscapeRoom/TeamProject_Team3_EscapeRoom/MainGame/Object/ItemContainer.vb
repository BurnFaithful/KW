Public Class ItemContainer
    Inherits Singleton(Of ItemContainer)

    Private itemList As New List(Of Item)
    Public ReadOnly Property pItemList As List(Of Item)
        Get
            Return itemList
        End Get
    End Property

    Public Sub AddItem(_id As Integer)
        itemList.Add(New Item(_id))
    End Sub

    Public Sub AddItem(_itemKind As Item.eItemKind, _id As Integer, _name As String,
                   Optional _image As Image = Nothing)
        itemList.Add(New Item(_itemKind, _id, _name, _image))
    End Sub

    Public Function RemoveItem(_id As Integer) As Boolean
        For i = 0 To itemList.Count - 1
            If itemList.Item(i).pId = _id Then
                itemList.RemoveAt(i)
                Return True
            End If
        Next

        Return False
    End Function

    Public Function GetItem(_id As Integer)
        For i = 0 To itemList.Count - 1
            If itemList.Item(i).pId = _id Then
                Return itemList.Item(i)
            End If
        Next

        Return Nothing
    End Function
End Class
