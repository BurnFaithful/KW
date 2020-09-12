Public Class DialogManager
    Inherits Singleton(Of DialogManager)

    Private dialogBox As TextBox
    Private okButton As Button
    Private dialogList As New List(Of Dialog)
    Private isPrintStart As Boolean

    Private textEnumerator As IEnumerator
    Public Property pTextEnumerator As IEnumerator
        Get
            Return textEnumerator
        End Get
        Set(value As IEnumerator)
            textEnumerator = value
        End Set
    End Property

    Public Sub Init()
        dialogBox = New TextBox() With
            {
                .Multiline = True,
                .ReadOnly = True,
                .Font = New Font(Form.DefaultFont.FontFamily, 15, FontStyle.Bold),
                .Width = 400,
                .Height = 200,
                .Location = New Point(450, 0)
            }
        MainForm.pUiPanel.Controls.Add(dialogBox)

        ' Temp
        Dim dialogNum As Integer = DATA_DIALOG_STARTNUM + DialogData.GetInstance().GetRowCount() - 1
        For i = DATA_DIALOG_STARTNUM To dialogNum
            AddDialog(i + 1)
        Next

        textEnumerator = dialogList(0).pClearText.GetEnumerator()
    End Sub

    Public Sub AddDialog(_id As Integer)
        Dim data As DataElement = Nothing
        If DialogData.GetInstance().FindElementByKey("Id", _id, data) Then
            Dim item As New Dialog With
            {
                .pId = _id,
                .pClearText = data.DataIndexer("ClearText").value,
                .pNormalTExt = data.DataIndexer("NormalText").value
            }
            dialogList.Add(item)
        End If
    End Sub

    Public Function GetClearDialog(_id As Integer) As String
        For Each var In dialogList
            If var.pId = _id Then
                Return var.pClearText
            End If
        Next

        Return String.Empty
    End Function

    Public Function GetNormalDialog(_id As Integer) As String
        For Each var In dialogList
            If var.pId = _id Then
                Return var.pNormalTExt
            End If
        Next

        Return String.Empty
    End Function

    Public Sub PrintDialog()
        If textEnumerator.MoveNext() Then
            dialogBox.Text &= textEnumerator.Current
        Else
            MainForm.DialogTimer.Enabled = False
        End If
    End Sub

    Public Sub ClearDialogBox()
        dialogBox.Clear()
    End Sub
End Class
