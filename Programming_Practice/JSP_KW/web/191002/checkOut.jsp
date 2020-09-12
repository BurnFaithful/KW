<%@ page import="java.util.ArrayList" %><%--
  Created by IntelliJ IDEA.
  User: user
  Date: 2019-10-02
  Time: 오후 2:29
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <meta charset="UTF-8">
    <title>구매상품 리스트 출력</title>
</head>
<body>
    <div align="center">
        <h2>계산</h2>
        선택한 상품 목록
        <hr>
        <%
            ArrayList productList = (ArrayList)session.getAttribute("productlist");
            if (productList == null)
                out.println("선택한 상품이 없습니다.<br>");
            else
            {
                for (Object productName:productList)
                    out.println(productName + "<br>");
            }
        %>
    </div>
</body>
</html>
