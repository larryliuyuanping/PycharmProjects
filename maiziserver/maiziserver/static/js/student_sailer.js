/**
 * Created by Administrator on 2017/3/6.
 */

function onQuery()
{
    var account =  _getQueryValue($("#txtAccount").val());
    var student_name =  _getQueryValue($("#txtStudentName").val());
    var sailer =  _getQueryValue($("#txtSailer").val());
    var phone =  _getQueryValue($("#txtPhone").val());
    var qq =  _getQueryValue($("#txtQQ").val());

    var pageSize = $("#slctPageSize").val();
    var params = "account="+account;
    params += "&student_name="+student_name;
    params += "&sailer="+sailer;
    params += "&phone="+phone;
    params += "&qq="+qq;
    params += "&page_size=" + pageSize
    window.location.href = "/student_sailer/?" + params ;
}

function onAddSail()
{
    window.location.href = "/student_sailer/add/";
}

function onUpdateSail(id)
{
    window.location.href = "/student_sailer/update/?id=" + id;
}

function onAddDo()
{
        var account = $("#txtAccount").val();
        var student_name = $("#txtStudentName").val();
        var phone = $("#txtPhone").val();
        var qq = $("#txtQQ").val();
        var address = $("#txtAddress").val();
        var pay_money = $("#txtPayMoney").val();
        var pay_type = $("#txtPayType").val();
        var sailer = $("#txtSailer").val();
        var sail_at = $("#txtSailAt").val();
        var sail_remark = $("#txtSailRemark").val();
        var student_remark = $("#txtStudentRemark").val();

        var career_id = $("#slctCareer").val();
        var career_job = $("input[name='rdoCareerJob']:checked").val();
        var assistant_id = $("#slctAssistant").val();
        var teacher_id = $("#slctTeacher").val();

        var reward = $("input[name='rdoReward']:checked").val();
        var reward_month = $("#slctRewardMonth").val();
        var bank = $("#txtBank").val();
        var bank_account = $("#txtBankAccount").val();
        var idcard = $("#txtIDCard").val();

        var loan = $("input[name='rdoLoan']:checked").val();
        var loan_company = $("#txtLoanCompany").val();
        var loan_type = $("#txtLoanType").val();
        var loan_interest = $("#txtLoanInterest").val();
        var loan_person = $("#txtLoanPerson").val();
        var loan_money = $("#txtLoanMoney").val();
        var subsidy = $("#txtSubsidy").val();
        var reduction = $("#txtReduction").val();

        if (_checkStringLength(account,2,20) == false) {
            _alertDialog("提示","麦子账号在2~50个字符之间");
            return;
        }

        if (_checkStringLength(student_name,2,10) == false) {
            _alertDialog("提示","学员姓名在2~10个字符之间");
            return;
        }

        if (_checkPhone(phone) == false) {
            _alertDialog("提示","请输入正确的手机号");
            return;
        }

        if (_checkStringLength(qq,2,20) == false) {
            _alertDialog("提示","qq在2~20个字符之间");
            return;
        }

        if (_checkStringLength(address,2,20) == false) {
            _alertDialog("提示","所在地在2~20个字符之间");
            return;
        }
        if (career_id == "") {
            _alertDialog("提示","请选择所学专业");
            return;
        }

        if (career_job == "") {
            _alertDialog("提示","请选择就业类型");
            return;
        }

        if (_isInteger(pay_money) == false) {
            _alertDialog("提示","支付金额请输入正整数");
            return;
        }

        if (_checkStringLength(pay_type,2,20) == false) {
            _alertDialog("提示","支付方式在2~10个字符之间");
            return;
        }

        if (_isDate(sail_at) == false) {
            _alertDialog("提示","成单日期请以2018-08-18的格式");
            return;
        }

        if (teacher_id == "") {
            _alertDialog("提示","请选择技术老师");
            return;
        }

        if (assistant_id == "") {
            _alertDialog("提示","请选择教务老师");
            return;
        }

        if (_checkStringLength(sail_remark,10,500) == false) {
            _alertDialog("提示","销售备注在10~500个字符之间");
            return;
        }

        if (_checkStringLength(student_remark,10,500) == false) {
            _alertDialog("提示","学员概况在10~500个字符之间");
            return;
        }
        $.post("/student_sailer/add/do/",
            {
                account : account,
                student_name : student_name,
                phone : phone,
                qq : qq,
                address : address,
                pay_money : pay_money,
                pay_type : pay_type,
                sailer : sailer,
                sail_at : sail_at,
                sail_remark : sail_remark,
                student_remark : student_remark,
                career_id : career_id,
                career_job : career_job,
                assistant_id : assistant_id,
                teacher_id : teacher_id,
                reward:reward,
                reward_month:reward_month,
                bank:bank,
                bank_account:bank_account,
                idcard:idcard,
                loan:loan,
                loan_company:loan_company,
                loan_type:loan_type,
                loan_interest:loan_interest,
                loan_person:loan_person,
                loan_money:loan_money,
                subsidy:subsidy,
                reduction:reduction
            },
            function (data, status) {
                if (data.code == 200) {
                    if (data.success) {
                        window.location.href = "/add/success/?op_url=/student_sailer/add/&return_url=/student_sailer/";
                    }
                    else {
                        _alertDialog("提示",data.message);
                    }
                }
            });
}

function onUpdateDo()
{
        var student_id = $('#txtStudentID').val();

        var account = $("#txtAccount").val();
        var student_name = $("#txtStudentName").val();
        var phone = $("#txtPhone").val();
        var qq = $("#txtQQ").val();
        var address = $("#txtAddress").val();
        var pay_money = $("#txtPayMoney").val();
        var pay_type = $("#txtPayType").val();
        var sailer = $("#txtSailer").val();
        var sail_at = $("#txtSailAt").val();
        var sail_remark = $("#txtSailRemark").val();
        var student_remark = $("#txtStudentRemark").val();

        var career_id = $("#slctCareer").val();
        var career_job = $("input[name='rdoCareerJob']:checked").val();
        var assistant_id = $("#slctAssistant").val();
        var teacher_id = $("#slctTeacher").val();

        var reward = $("input[name='rdoReward']:checked").val();
        var reward_month = $("#slctRewardMonth").val();
        var bank = $("#txtBank").val();
        var bank_account = $("#txtBankAccount").val();
        var idcard = $("#txtIDCard").val();

        var loan = $("input[name='rdoLoan']:checked").val();
        var loan_company = $("#txtLoanCompany").val();
        var loan_type = $("#txtLoanType").val();
        var loan_interest = $("#txtLoanInterest").val();
        var loan_person = $("#txtLoanPerson").val();
        var loan_money = $("#txtLoanMoney").val();
        var subsidy = $("#txtSubsidy").val();
        var reduction = $("#txtReduction").val();

        if (_checkStringLength(account,2,20) == false) {
            _alertDialog("提示","麦子账号在2~50个字符之间");
            return;
        }

        if (_checkStringLength(student_name,2,10) == false) {
            _alertDialog("提示","学员姓名在2~10个字符之间");
            return;
        }

        if (_checkPhone(phone) == false) {
            _alertDialog("提示","请输入正确的手机号");
            return;
        }

        if (_checkStringLength(qq,2,20) == false) {
            _alertDialog("提示","qq在2~20个字符之间");
            return;
        }

        if (_checkStringLength(address,2,20) == false) {
            _alertDialog("提示","所在地在2~20个字符之间");
            return;
        }
        if (career_id == "") {
            _alertDialog("提示","请选择所学专业");
            return;
        }

        if (career_job == "") {
            _alertDialog("提示","请选择就业类型");
            return;
        }

        if (_isInteger(pay_money) == false) {
            _alertDialog("提示","支付金额请输入正整数");
            return;
        }

        if (_checkStringLength(pay_type,2,20) == false) {
            _alertDialog("提示","支付方式在2~10个字符之间");
            return;
        }

        if (_isDate(sail_at) == false) {
            _alertDialog("提示","成单日期请以2018-08-18的格式");
            return;
        }

        if (teacher_id == "") {
            _alertDialog("提示","请选择技术老师");
            return;
        }

        if (assistant_id == "") {
            _alertDialog("提示","请选择教务老师");
            return;
        }

        if (_checkStringLength(sail_remark,10,500) == false) {
            _alertDialog("提示","销售备注在10~500个字符之间");
            return;
        }

        if (_checkStringLength(student_remark,10,500) == false) {
            _alertDialog("提示","学员概况在10~500个字符之间");
            return;
        }

        $.post("/student_sailer/update/do/",
            {
                id : student_id,
                account : account,
                student_name : student_name,
                phone : phone,
                qq : qq,
                address : address,
                pay_money : pay_money,
                pay_type : pay_type,
                sailer : sailer,
                sail_at : sail_at,
                sail_remark : sail_remark,
                student_remark : student_remark,
                career_id : career_id,
                career_job : career_job,
                assistant_id : assistant_id,
                teacher_id : teacher_id,
                reward:reward,
                reward_month:reward_month,
                bank:bank,
                bank_account:bank_account,
                idcard:idcard,
                loan:loan,
                loan_company:loan_company,
                loan_type:loan_type,
                loan_interest:loan_interest,
                loan_person:loan_person,
                loan_money:loan_money,
                subsidy:subsidy,
                reduction:reduction
            },
            function (data, status) {
                if (data.code == 200) {
                    if (data.success) {
                        window.location.href = "/update/success/?return_url=/student_sailer/";
                    }
                    else {
                        _alertDialog("提示",data.message);
                    }
                }
            });
}

function onReturn()
{
    window.location.href = "/student_sailer/";
}

