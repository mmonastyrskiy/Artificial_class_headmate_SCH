#ifndef DEPLOYDATAMENU_H
#define DEPLOYDATAMENU_H

#include <QMainWindow>
#include <QtSql/QSql>
#include <QtSql/QSqlDatabase>
namespace Ui {
class DeployDataMenu;
}

class DeployDataMenu : public QMainWindow
{
    Q_OBJECT

public:
    explicit DeployDataMenu(QWidget *parent = nullptr);
    ~DeployDataMenu();
//virtual QVariant data(const QModelIndex &item, int role);
private slots:
    void on_Export_Butt_clicked();

    void on_In_Butt_clicked();

    void on_OUT_Butt_clicked();

    void on_LATE_but_clicked();

    void on_Plort_Butt_clicked();



void on_Exit_Button_clicked();

void on_Exit_Button_clicked(bool checked);

private:
    Ui::DeployDataMenu *ui;
     void refresh();
     void getWasInSchool( QString id);
     void getWasOutSchool( QString id);
     void getWasLateSchool( QString id);
};

#endif // DEPLOYDATAMENU_H
