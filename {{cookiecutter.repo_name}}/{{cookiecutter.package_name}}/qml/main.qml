import QtQuick 2.15
import QtQuick.Window 2.15

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("{{ cookiecutter.application_title }}")

    Text {
        id: text
        text: qsTr("{{ cookiecutter.application_name }}")
        anchors.centerIn: parent
    }
}
