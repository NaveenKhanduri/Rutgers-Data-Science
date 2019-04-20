Attribute VB_Name = "Module1"
Sub stockCount()

'Declare variables

Dim ws As Worksheet
Dim i As Long
Dim change As Double
Dim percent As Double
Dim sheetLength As Long
Dim volume As Double
'Dim tagCol As Long
Dim count As Long
Dim op As Double
Dim clo As Double
Dim greatest As Double
Dim least As Double
Dim greattag As String
Dim leasttag As String

For Each ws In ActiveWorkbook.Worksheets

    
    ws.Range("H:H").Clear
    ws.Range("I:I").Clear
    ws.Range("j:j").Clear
    ws.Range("K:K").Clear
    ws.Range("L:L").Clear
    ws.Range("M:M").Clear
    ws.Range("N:N").Clear
    
    count = 2
    ws.Cells(1, 11).Value = "yearly difference"
    ws.Cells(1, 12).Value = "percent change"
    ws.Cells(1, 9).Value = "tag"
    ws.Cells(1, 10).Value = "total Volume"

    
    greatest = 0  'default values for least and greatest percent change
    least = 0
    
    

    sheetLength = ws.Cells(Rows.count, 1).End(xlUp).Row
    op = ws.Cells(2, 3).Value


    For i = 2 To sheetLength
    
   'this loop iteration runs every time a new tag is encountered
    If (ws.Cells(i, 1).Value <> ws.Cells(i + 1, 1).Value) Then
        ws.Cells(count, 9).Value = ws.Cells(i, 1).Value
        volume = volume + ws.Cells(i, 7).Value
        ws.Cells(count, 10).Value = volume
        clo = ws.Cells(i, 6).Value
        
        change = (clo - op)
                
        If (op <> 0) Then
            percent = (change / op)
            
        Else
            percent = 0
        End If
        
        If (greatest < percent) Then
            greatest = percent
            greattag = ws.Cells(i, 1).Value
        ElseIf (percent < least) Then
           least = percent
           leasttag = ws.Cells(i, 1).Value
           
        End If
        
        ws.Cells(count, 11).Value = change
        ws.Cells(count, 12).Value = percent
        ws.Cells(count, 12).NumberFormat = "0.00%"
            If (change < 0) Then
                ws.Cells(count, 11).Interior.Color = vbRed
                ws.Cells(count, 12).Interior.Color = vbRed
             Else
                ws.Cells(count, 11).Interior.Color = vbGreen
                ws.Cells(count, 12).Interior.Color = vbGreen
            End If
       'ws.Cells(count, 13).Value = Str(clo) + ": clo--" + Str(op) + ": op"
       count = count + 1
       op = ws.Cells(i + 1, 3).Value
       'reset volume to zero
       volume = 0
       
    Else
        volume = volume + ws.Cells(i, 7).Value
    End If
       
    Next i
    
ws.Cells(1, 15).Value = "Tag"
ws.Cells(1, 16).Value = "percent change"
ws.Cells(2, 14).Value = "Greatest Percent Change"
ws.Cells(2, 15).Value = greattag
ws.Cells(2, 16).Value = greatest
ws.Cells(2, 16).NumberFormat = "0.00%"
ws.Cells(3, 14).Value = "Least Percent Change"
ws.Cells(3, 15).Value = leasttag
ws.Cells(3, 16).Value = least
ws.Cells(3, 16).NumberFormat = "0.00%"


Next ws

End Sub
