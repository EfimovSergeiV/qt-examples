import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")

    Label {
        id: label
        x: 5
        y: 80
        width: 322
        height: 48
        text: qsTr("0")
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        font.pointSize: 18
        font.bold: true
    }

    Label {
        id: label1
        x: 333
        y: 80
        width: 299
        height: 48
        text: qsTr("0")
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        font.bold: true
        font.pointSize: 18
    }

    Button {
        id: button
        x: 5
        y: 220
        width: 211
        height: 40
        text: qsTr("Run first worker")
        onClicked: {
            handler.first_worker_start()
        }
    }

    Button {
        id: button1
        x: 433
        y: 220
        width: 199
        height: 40
        text: qsTr("Run second worker")
        onClicked: {
            handler.second_worker_start()
        }
    }

    Connections {
        target: handler

        function onFirstWorker(value) {
            label.text = value
        }

        function onSecondWorker(value) {
            label1.text = value
        }
    }

    Button {
        id: button2
        x: 222
        y: 244
        width: 205
        height: 40
        text: qsTr("Check frieze")
    }

    Button {
        id: button3
        x: 5
        y: 266
        width: 211
        height: 40
        text: qsTr("Stop first worker")
        onClicked: {
            handler.first_worker_stop()
        }
    }

    Button {
        id: button4
        x: 433
        y: 266
        width: 199
        height: 40
        text: qsTr("Stop second worker")
        onClicked: {
            handler.second_worker_stop()
        }
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.75}D{i:2}
}
##^##*/
