Public Class Inventory
    Inherits Singleton(Of Inventory)

    Public Const slotLimitCnt As Integer = 4

    Public Structure tagSlot
        Dim itemInfo As Item
        Dim isEmpty As Boolean
        Dim slotPB As PictureBox
    End Structure

    Private slot(slotLimitCnt - 1) As tagSlot

    Public Sub Init()
        Dim tempGameScene As GameScene = SceneManager.GetInstance().GetSceneByKey("Game")

        For i = 0 To UBound(slot)
            slot(i).isEmpty = True
            slot(i).slotPB = New PictureBox() With
            {
                .Width = 100,
                .Height = 100,
                .BackColor = Color.Gray
            }
            slot(i).slotPB.Location = New Point((slot(i).slotPB.Width + 10) * i, 0)
            MainForm.pUiPanel.Controls.Add(slot(i).slotPB)
        Next
    End Sub

    Public Sub AddItem(_item As Item)
        For i = 0 To UBound(slot)
            If slot(i).isEmpty = True Then
                _item.pParentSlotnum = i
                _item.pPB.Width = slot(i).slotPB.Width
                _item.pPB.Height = slot(i).slotPB.Height
                slot(i).slotPB.Controls.Add(_item.pPB)
                slot(i).itemInfo = _item
                slot(i).isEmpty = False
                Exit For
            End If
        Next
    End Sub

    Public Function GetItem(_item As Item) As Item
        For i = 0 To UBound(slot)
            If slot(i).itemInfo Is _item Then
                Return slot(i).itemInfo
            End If
        Next

        Return Nothing
    End Function

    Public Function GetItem(_id As Integer) As Item
        For i = 0 To UBound(slot)
            If slot(i).itemInfo.pId = _id Then
                Return slot(i).itemInfo
            End If
        Next

        Return Nothing
    End Function

    Public Sub RemoveItem(_item As Item)
        For i = 0 To UBound(slot)
            If slot(i).itemInfo Is _item Then
                slot(i).itemInfo = Nothing
                slot(i).slotPB.Controls.Remove(_item.pPB)
                slot(i).isEmpty = True
                Exit For
            End If
        Next
    End Sub

    Public Sub RemoveAtItem(index As Integer)
        slot(index).itemInfo = Nothing
        slot(index).slotPB.Controls.RemoveAt(0)
        slot(index).isEmpty = True
    End Sub

    Public Function RemoveItemById(_id As Integer) As Boolean
        For i = 0 To UBound(slot)
            If slot(i).itemInfo IsNot Nothing Then
                If slot(i).itemInfo.pId = _id Then
                    slot(i).itemInfo = Nothing
                    slot(i).slotPB.Controls.RemoveAt(0)
                    slot(i).isEmpty = True
                    Return True
                End If
            End If
        Next

        Return False
    End Function

    Public Function IsFull() As Boolean
        For i = 0 To UBound(slot)
            If slot(i).isEmpty = True Then
                Return False
            End If
        Next

        Return True
    End Function
End Class
