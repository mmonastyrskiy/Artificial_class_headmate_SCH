#include "deploydatamenu.h"
#include "ui_deploydatamenu.h"
#include <QFileDialog>
#include <QtSql/QSql>
#include<QtSql/QSqlDatabase>
#include <QtSql/QSqlQueryModel>
#include<QtSql/QSqlQuery>
#include <QDebug>
DeployDataMenu::DeployDataMenu(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::DeployDataMenu)
{

    //QSqlDatabase db = QSqlDatabase::addDatabase("QPSQL");
    //db.setDatabaseName("SCH_DB");
    //db.setHostName("schdb.sch");
    //db.setUserName("root");
    //db.setPassword("DBpassword");
    //if(!db.open()){
        //qDebug() << "Failed";
        //system("pause");
        //db.close();
    ui->setupUi(this);
    }

DeployDataMenu::~DeployDataMenu()
{
    delete ui;
}




void DeployDataMenu::on_Export_Butt_clicked()
{
    QString Path =  QFileDialog::getExistingDirectory(this, tr("Choose catalog"), ".", QFileDialog::ReadOnly);
}

void DeployDataMenu::on_In_Butt_clicked()
{
    //QSqlQueryModel *model = new QSqlQueryModel;
   // QSqlQuery *qry = new QSqlQuery;
    //QString s = ui->comboBox->currentText();
    //qry->prepare("SELECT * FROM " +s+ " WHERE IsInSchool=1");
    //qry->exec();
    //model->setQuery(*qry);
    //ui->tableView->setModel(model);

   system("InSchool.bat");
}

void DeployDataMenu::on_OUT_Butt_clicked()
{
    //QSqlQueryModel *model = new QSqlQueryModel;
   // QSqlQuery *qry = new QSqlQuery;
    //QString s = ui->comboBox->currentText();
    //qry->prepare("SELECT * FROM " +s+ " WHERE IsInSchool=0");
    //qry->exec();
    //model->setQuery(*qry);
    //ui->tableView->setModel(model);

    system("OutSchool.bat");
}

void DeployDataMenu::on_LATE_but_clicked()
{
    //QSqlQueryModel *model = new QSqlQueryModel;
    //QSqlQuery *qry = new QSqlQuery;
    //QString s = ui->comboBox->currentText();
    //qry->prepare("SELECT * FROM" +s+ "WHERE Timestapm > 30000");
    //qry->exec();
    //model->setQuery(*qry);
    //ui->tableView->setModel(model);

    system("LateSchool.bat");
}

void DeployDataMenu::on_Plort_Butt_clicked()
{
    system("Build.bat");
}

void DeployDataMenu::on_Exit_Button_clicked()
{
   // db.close();
    //this->close();
}

void DeployDataMenu::on_Exit_Button_clicked(bool checked)
{
   // db.close();
}
