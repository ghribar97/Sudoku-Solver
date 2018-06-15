from GUI.captureVideo import CaptureVideo
from GUI.capureImageView import CaptureImageView
import cv2
from unittest import TestCase


class CaptureVideoTester(TestCase):
    def test_del(self):
        master = CaptureImageView
        video = CaptureVideo(master)
        before = video.video.isOpened()
        video.__del__()
        after = video.video.isOpened()
        self.assertNotEqual(before, after)

    def test_init(self):
        master = CaptureImageView
        video = CaptureVideo(master)
        self.assertEqual(video.video_source, 0)
        self.assertEqual(video.parent_window, master)
        self.assertEqual(type(video.video), type(cv2.VideoCapture()))
        self.assertEqual(video.width, video.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.assertEqual(video.height, video.video.get(cv2.CAP_PROP_FRAME_HEIGHT)
)
