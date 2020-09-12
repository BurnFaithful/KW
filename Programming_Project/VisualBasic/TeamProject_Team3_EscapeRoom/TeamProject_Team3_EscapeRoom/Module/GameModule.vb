Module GameModule

    Public Const WINDOWS_NAME As String = "The Rum"
    Public Const GAME_STARTSCENE As String = "Title"

    Public Const WINDOWS_WIDTH As Integer = 1024
    Public Const WINDOWS_HEIGHT As Integer = 768

    Public Const UP_WHEEL_VALUE As Short = 120
    Public Const DOWN_WHEEL_VALUE As Short = -120

    Public Const DATA_ITEM_STARTNUM As Integer = 100
    Public Const DATA_DIALOG_STARTNUM As Integer = 1000
    Public Const DATA_SUBFORM_STARTNUM As Integer = 10000

    Private rndGenerator As New Random

    Public Function RandomInt(maxValue As Integer)
        Return rndGenerator.Next(0, maxValue)
    End Function

    Public Function RandomInt(minValue As Integer, maxValue As Integer)
        Return rndGenerator.Next(minValue, maxValue)
    End Function

    Public Function RandomDouble(maxValue As Double)
        Return rndGenerator.NextDouble() * maxValue
    End Function

    Public Function AbsInt_Custom(value As Integer)
        If value < 0 Then
            Return -value
        End If
        Return value
    End Function

    Public Function AbsDouble_Custom(value As Double)
        If value < 0.0F Then
            Return -value
        End If
        Return value
    End Function

    Public Function GetResourceImage(fileName As String) As Image
        Return MainForm.rm.GetObject(fileName)
    End Function
End Module
