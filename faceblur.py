#!/usr/bin/python2

# This work is released under public domain.
# Contact: oleander@oleander.cc
# github: https://github.com/fleischhoernchen/faceblur

import sys
import cv

def detectObject(image):
	grayscale = cv.CreateImage((image.width, image.height), 8, 1)
	cv.CvtColor(image, grayscale, cv.CV_BGR2GRAY)
	storage = cv.CreateMemStorage(0)
	# depcrecated?
	#cv.ClearMemStorage(storage)
	cv.EqualizeHist(grayscale, grayscale)
	cascade = cv.Load('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')
	faces = cv.HaarDetectObjects(grayscale, cascade, storage, 1.2, 2, cv.CV_HAAR_DO_CANNY_PRUNING, (100,100))

	if len(faces) > 0:
		print(faces)
		for i in faces:
			i = i[0]
			print("[(%d,%d) -> (%d,%d)]" % (i[0], i[1], i[0]+i[2], i[1]+i[3]))
			face = cv.GetSubRect(image, (i[0], i[1], i[2], i[3]))
			cv.Smooth(face, face, cv.CV_BLUR, intens)
			cv.ResetImageROI(image)

	cascade = cv.Load('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')
	faces = cv.HaarDetectObjects(grayscale, cascade, storage, 1.2, 2, cv.CV_HAAR_DO_CANNY_PRUNING, (100,100))

	if len(faces) > 0:
		print(faces)
		for i in faces:
			i = i[0]
			print("[(%d,%d) -> (%d,%d)]" % (i[0], i[1], i[0]+i[2], i[1]+i[3]))
			face = cv.GetSubRect(image, (i[0], i[1], i[2], i[3]))
			cv.Smooth(face, face, cv.CV_BLUR, intens)
			cv.ResetImageROI(image)

	cascade = cv.Load('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt2.xml')
	faces = cv.HaarDetectObjects(grayscale, cascade, storage, 1.2, 2, cv.CV_HAAR_DO_CANNY_PRUNING, (100,100))

	if len(faces) > 0:
		print(faces)
		for i in faces:
			i = i[0]
			print("[(%d,%d) -> (%d,%d)]" % (i[0], i[1], i[0]+i[2], i[1]+i[3]))
			face = cv.GetSubRect(image, (i[0], i[1], i[2], i[3]))
			cv.Smooth(face, face, cv.CV_BLUR, intens)
			cv.ResetImageROI(image)

class closeWindow(object):
	def __call__(self, check):
		global ok
		if check < 5:
			ok = 0
			cv.DestroyWindow(("Kontrolle - %s @ %i" % (sys.argv[1], intens)))

		elif check > 195:
			ok = 1
			cv.DestroyWindow(("Kontrolle - %s @ %i" % (sys.argv[1], intens)))


def displayObject(image):
	cv.NamedWindow(("Kontrolle - %s @ %i" % (sys.argv[1], intens)), 0)
	cv.ResizeWindow(("Kontrolle - %s @ %i" % (sys.argv[1], intens)), 800, 480)
	cv.ShowImage(("Kontrolle - %s @ %i" % (sys.argv[1], intens)), image)

	global ok
	ok = 0
	cv.CreateTrackbar("OK? (links nein, rechts ja)", ("Kontrolle - %s @ %i" % (sys.argv[1], intens)), 100, 200, closeWindow())

	cv.WaitKey(0)
	cv.DestroyWindow(("Kontrolle - %s @ %i" % (sys.argv[1], intens)))
  
def main():
	global intens
	if len(sys.argv) == 3:
		intens = int(sys.argv[2])
	elif len(sys.argv) == 2:
		intens = 25
	else:
		exit('./blur2.py bilddatei (intensitaet)')

	image = cv.LoadImage(sys.argv[1])
	detectObject(image)
	displayObject(image)

	if ok == 1:
		end = sys.argv[1].split(".", 1)
		print("Gespeichert: %s_blurred.%s" % (end[0], end[-1]))
		cv.SaveImage(("%s_blurred.%s" % (end[0], end[-1])), image)

if __name__ == "__main__":
  main()
