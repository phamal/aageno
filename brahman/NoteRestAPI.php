  <?php

include "beans/NoteBean.php";
$data = file_get_contents("php://input");
$objData = json_decode($data);
$noteBean = new NoteBean();
switch ($objData->action) {
    case "getNotes":
        echo json_encode($noteBean->getNotes());
        break;
    case "addNote":
        $noteBean->addNote($objData->note);
        $data = array("msg" => "Successfully saved added the note" . $objData->note);
        echo json_encode($data);
        break;
    case "deleteNote":
        $noteBean->deleteNote($objData->noteId);
        $data = array("success" => "true", "msg" => "Successfully deleted the note");
        echo json_encode($data);
        break;
    case "searchNoteWithHashTag":
        $data = $noteBean->searchNoteWithHashTag($objData->hashtag);
        echo json_encode($data);
        break;
    case "getHashTags":
        echo json_encode($noteBean->getHashTags());
        break;
    case "converse":
        $answer = $noteBean->interact($objData->question);
        $data = array("answer" => $answer);
        echo json_encode($data);
        break;
}
?>

