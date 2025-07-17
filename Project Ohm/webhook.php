<?php
// รับข้อมูลจาก LINE
$raw = file_get_contents('php://input');

// บันทึก Log เผื่อดูย้อนหลัง
file_put_contents('webhook_log.json', $raw . PHP_EOL, FILE_APPEND);

// แปลง JSON เป็น array
$data = json_decode($raw, true);

// ตรวจจับ userId และบันทึกไว้
if (isset($data['events'])) {
    foreach ($data['events'] as $event) {
        if (!empty($event['source']['userId'])) {
            $userId = $event['source']['userId'];
            $file = 'user_ids.txt';

            // อ่าน user เดิม
            $list = file_exists($file) ? file($file, FILE_IGNORE_NEW_LINES) : [];

            // ถ้ายังไม่เคยมี → เพิ่มใหม่
            if (!in_array($userId, $list)) {
                file_put_contents($file, $userId . PHP_EOL, FILE_APPEND);
                error_log("✅ เพิ่ม userId ใหม่: $userId");
            }
        }
    }
}

http_response_code(200);
echo 'OK';
?>
