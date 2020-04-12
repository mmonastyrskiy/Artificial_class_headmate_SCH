#include "choosemode.h"
#include "ui_choosemode.h"

ChooseMode::ChooseMode(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::ChooseMode)
{
    ui->setupUi(this);
    cont = new Controls;
    ddm = new DeployDataMenu;
}

ChooseMode::~ChooseMode()
{
    delete ui;
}

void ChooseMode::on_pushButton_clicked()
{
    cont->show();
    this->close();
}

void ChooseMode::on_pushButton_2_clicked()
{
    ddm->show();
    this->close();
}
