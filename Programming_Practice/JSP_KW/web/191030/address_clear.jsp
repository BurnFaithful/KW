<%--
  Created by IntelliJ IDEA.
  User: user
  Date: 2019-10-30
  Time: 오후 4:09
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="youngmin.address.AddressManager" %>
<jsp:useBean id="addressList" class="youngmin.address.AddressManager" scope="application"/>

<%
    addressList.Clear();
%>
<html>
<head>
    <title>AddressList Clear</title>
</head>
<body>
    <script>location.href = "address_form.html"</script>
</body>
</html>
