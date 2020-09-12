Public Class DataElement

    Public dataList As New List(Of DataItem)

    Default ReadOnly Property DataIndexer(ByVal keyword As String) As DataItem
        Get
            For i = 0 To dataList.Count - 1
                If dataList(i).key = keyword Then
                    Return dataList(i)
                End If
            Next

            Return Nothing
        End Get
    End Property
End Class

Public Class DataItem
    Public key As String
    Public value As String
End Class
