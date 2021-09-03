function ListAllCourseWork(){
    var response = Classroom.Courses.CourseWork.list(CourseId);
    var json = JSON.parse(response.courseWork[0])
    var res = json.alternateLink
    return res;
}

function doGet(e) {
  var res = ListAllCourseWork()
  var data = {url:res};
  var payload = JSON.stringify(data)
  var output = ContentService.createTextOutput();
  output.setMimeType(ContentService.MimeType.JSON);
  output.setContent(payload);
  
  return output;
}
