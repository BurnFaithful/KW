<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<style type="text/css">
		img
		{
			width: 25%;
			height: 30%;
		}
	</style>
	<script type="text/javascript">
		var whopper = false;
		var coke = false;
		var fries = false;
		var total = 0;
	
		function printPrice()
		{
			if (document.getElementById("whopper"))
			{
				alert("와퍼 4500원");
				whopper = true;
			}
			else if (document.getElementById("coke"))
			{
				alert("콜라 2000원");
				coke = true;
			}
			else if (document.getElementById("fries"))
			{
				alert("감자튀김 1000원");
				fries = true;
			}
		}
		
		function totalPrice()
		{
			if (whopper == true) total += 4500;
			if (coke == true) total += 2000;
			if (fries == true) total += 1000;
			document.write(total);
		}
		
		function reset()
		{
			whopper = false;
			coke = false;
			fries = false;
			total = 0;
		}
		
		// 교수님. 만들다 말았습니다.
	</script>
</head>
<body>
	<h3>버거킹을 먹읍시다.</h3>
	<img src="whopper.jpg" id="whopper" onclick="printPrice()">
	<img src="coke.jpg" id="coke" onclick="printPrice()">
	<img src="french-fries.jpg" id="fries" onclick="printPrice()"><br>
	
	<input type="submit" name="buy" value="구매" onclick="totalPrice()">
	<input type="reset" name="reselect" value="리셋" onclick="reset()">
	
	<script> document.write(total); </script>
</body>
</html>