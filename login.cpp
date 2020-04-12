#include "login.h"
#include "ui_login.h"
#include <QCryptographicHash>
#include <string>
using namespace std;
LogIn::LogIn(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::LogIn)
{
    ui->setupUi(this);
    cwindow = new ChooseMode;
}

LogIn::~LogIn()
{
    delete ui;
}


void LogIn::on_buttonBox_accepted()
{
    QString c;
    string login;
    QByteArray ba;
    if (c == ""){
        this->ui->label->setText("EMPTY FIELD");
    }
    c = this->ui->lineEdit->text();
    ba = c.toLocal8Bit();
    login = c.toUtf8().constData();
    if (QCryptographicHash::hash(ba,QCryptographicHash::Sha256).toHex() == QCryptographicHash::hash("111",QCryptographicHash::Sha256).toHex())
    {   cwindow->show();
        this->close();
    }
    else {
        this ->ui->label->setText("Wrong");
        this->ui->lineEdit->setText("");
    }
}
