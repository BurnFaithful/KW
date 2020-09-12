<%--
  Created by IntelliJ IDEA.
  User: user
  Date: 2019-11-13
  Time: 오후 1:25
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
<%@include file="file_header.jsp" %>
    <script src="../../js/page_func.js"></script>

    <title>리뷰 쓰기 페이지</title>

    <script>
        function validate()
        {
            var title = document.getElementById("review_bbsTitle");
            var content = document.getElementById("review_bbsContent");

            if (!title.value || !content.value)
            {
                alert("입력하지 않은 사항이 있습니다.");
                return false;
            }
            return true;
        }
    </script>
</head>
<body>
<%@include file="page_header.jsp" %>
<script>
    checkPage("${param.pageName}");
</script>

<div class="container">
    <div class="row">
        <form method="post" action="review_write_Action.jsp" onsubmit="return validate();">
            <table class="table table-striped" style="text-align: center; border: 1px solid #dddddd">
                <thead>
                    <tr>
                        <th colspan="2" style="background-color:#eeeeee; text-align: center;">리뷰 쓰기</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><input type="text" class="form-control" placeholder="영화 제목" id="review_bbsTitle" name="reviewTitle" maxlength="50"></td>
                    </tr>
                    <tr>
                        <td><textarea class="form-control" placeholder="리뷰 작성해주세요. 500자 미만." id="review_bbsContent" name="reviewContent" maxlength="500" style="height: 350px;"></textarea></td>
                    </tr>
                </tbody>
            </table>
            <input type="submit" class="btn btn-primary pull-right" value="글쓰기">
        </form>
    </div>
</div>

<%@include file="page_footer.jsp" %>
</body>
</html>
