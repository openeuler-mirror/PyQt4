%{!?python2_sitelib: %global python2_sitelib %(/usr/bin/python2 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch:%global python2_sitearch %(/usr/bin/python2 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%{!?python2_inc:%global python2_inc %(/usr/bin/python2 -c "from distutils.sysconfig import get_python_inc; print get_python_inc(1)")}
%{!?python3_inc:%global python3_inc %(%{__python3} -c "from distutils.sysconfig import get_python_inc; print(get_python_inc(1))")}
%global python2_dbus_dir %(/usr/bin/python2 -c "import dbus.mainloop; print(dbus.mainloop.__path__[0])")
%global python3_dbus_dir %(%{__python3} -c "import dbus.mainloop; print(dbus.mainloop.__path__[0])")
%global __provides_exclude_from ^(%{python2_sitearch}/.*\\.so|%{python3_sitearch}/.*\\.so|%{_qt4_plugindir}/.*\\.so)$
Name:          PyQt4
Version:       4.12.1
Release:       13
Summary:       Python bindings for Qt4
License:       (GPLv3 or GPLv2 with exceptions) and BSD
Url:           http://www.riverbankcomputing.com/software/pyqt/
Source0:       http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-%{version}/PyQt4_gpl_x11-%{version}.tar.gz

Patch0001:     qreal_float_support.diff
BuildRequires: chrpath dbus-python findutils gcc-c++ pkgconfig(dbus-1) pkgconfig(dbus-python) pkgconfig(phonon)
BuildRequires: pkgconfig(QtDBus) pkgconfig(QtDeclarative) pkgconfig(QtDesigner) pkgconfig(QtGui) pkgconfig(QtHelp)
BuildRequires: pkgconfig(QtMultimedia) pkgconfig(QtNetwork) pkgconfig(QtOpenGL) pkgconfig(QtScript) pkgconfig(QtScriptTools)
BuildRequires: pkgconfig(QtSql) pkgconfig(QtSvg) pkgconfig(QtTest) pkgconfig(QtXml) pkgconfig(QtXmlPatterns) python2-devel
BuildRequires: python2-sip python2-sip-devel >= 4.19 python3-dbus python3-devel python3-sip python3-sip-devel >= 4.19
Buildrequires: qt-assistant-adp-devel pkgconfig(QtWebKit)
Requires:      dbus-python qt4 >= %{_qt4_version} sip-api(%{_sip_api_major}) >= %{_sip_api}
Provides:      python-qt4 = %{version}-%{release} python2-qt4 = %{version}-%{release} python2-PyQt4 = %{version}-%{release}
Provides:      PyQt4-qsci-api = %{version}-%{release} PyQt4-assistant = %{version}-%{release} PyQt4-webkit = %{version}-%{release}
Provides:      python-qt4-qsci-api = %{version}-%{release} python2-qt4-qsci-api = %{version}-%{release} python2-pyqt4-qsci-api = %{version}-%{release}
Provides:      python-qt4-assistant = %{version}-%{release} python2-qt4-assistant = %{version}-%{release} python2-pyqt4-assistant = %{version}-%{release}
Provides:      python-qt4-webkit = %{version}-%{release} python2-qt4-webkit = %{version}-%{release} python2-PyQt4-webkit = %{version}-%{release}
Provides:      pyqt4-webkit = %{version}-%{release} pyqt4 = %{version}-%{release}
Obsoletes:     PyQt4 < 4.11.4-8 pyqt4-devel < 4.10.3-6 python3-pyqt4-devel < 4.10.3-6
Obsoletes:     PyQt4-qsci-api < %{version}-%{release} PyQt4-assistant < %{version}-%{release} PyQt4-webkit < %{version}-%{release}

%description
These are Python bindings for Qt4.

%package       devel
Summary:       Development files for the Qt4 library
Requires:      PyQt4 = %{version}-%{release} qt4-devel sip-devel
Provides:      PyQt4-webkit-devel = %{version}-%{release} python-qt4-devel = %{version}-%{release}
Provides:      python2-qt4-doc = %{version}-%{release} python2-PyQt4-doc = %{version}-%{release}
Provides:      pyqt4-devel = %{version}-%{release}
Obsoletes:     PyQt4 < 4.11.4-8 PyQt4-devel < 4.10.3-6 PyQt4-webkit-devel < %{version}-%{release}

%description   devel
The Qt4-devel package includes header files and libraries necessary for the Qt4 library.

%package       help
Summary:       This package contains help documents
BuildArch:     noarch
Requires:      PyQt4 = %{version}-%{release}
Provides:      PyQt4-doc = %{version}-%{release} python-qt4-doc = %{version}-%{release}
Provides:      python2-qt4-doc = %{version}-%{release} python2-PyQt4-doc = %{version}-%{release}
Obsoletes:     PyQt4-doc < %{version}-%{release} PyQt4-devel < 4.10.3-6 python3-PyQt4-devel < 4.10.3-6

%description   help
Files for help with PyQt4.

%package -n python3-PyQt4
Summary:       Python 3 bindings for Qt4
Requires:      python3-dbus python3-PyQt4 = %{version}-%{release} python3-PyQt4 = %{version}-%{release}
Requires:      qt4 >= %{_qt4_version} python3-sip-api(%{_sip_api_major}) >= %{_sip_api}
Provides:      python3-qt4 = %{version}-%{release} python3-qt4-assistant = %{version}-%{release} python3-qt4-webkit = %{version}-%{release}
Provides:      python3-PyQt4-assistant = %{version}-%{release} python3-PyQt4-webkit = %{version}-%{release}
Obsoletes:     python3-PyQt4 < 4.11.4-8 python3-PyQt4-assistant < %{version}-%{release} python3-PyQt4-webkit < %{version}-%{release}

%description -n python3-PyQt4
These are Python 3 bindings for Qt4.

%package -n python3-PyQt4-devel
Summary:       Python 3 bindings for Qt4
Provides:      python3-PyQt4-webkit-devel = %{version}-%{release} python3-qt4-devel = %{version}-%{release}
Requires:      python3-PyQt4 = %{version}-%{release} python3-sip-devel
Obsoletes:     python3-PyQt4-devel < 4.10.3-6

%description -n python3-PyQt4-devel
The python3-PyQt4-devel package includes header files and libraries necessary for the python3 PyQt4 library.

%prep
%autosetup -n PyQt4_gpl_x11-%{version} -p1
install -D ./sip/QtGui/opengl_types.sip ./sip/QtGui/opengl_types.sip.orig
find examples/ -name "*.py" | xargs chmod a-x

%build
QT4DIR=%{_qt4_prefix}
PATH=%{_qt4_bindir}:$PATH ; export PATH
install -d %{_target_platform}
cd %{_target_platform}
/usr/bin/python2 ../configure.py --assume-shared --confirm-license --no-timestamp --qmake=%{_qt4_qmake} --qsci-api \
  --qsci-api-destdir=%{_qt4_datadir}/qsci --verbose CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" LFLAGS="%{?__global_ldflags}"
%make_build
cd ..
install -d %{_target_platform}-python3
cd %{_target_platform}-python3
%{__python3} ../configure.py --assume-shared --confirm-license --no-timestamp --qmake=%{_qt4_qmake} --no-qsci-api \
  --sipdir=%{_datadir}/python3-sip/PyQt4 --verbose CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" LFLAGS="%{?__global_ldflags}"
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot} -C %{_target_platform}-python3
%make_install -C %{_target_platform}
rm -rfv %{buildroot}%{python2_sitearch}/PyQt4/uic/port_v3/
rm -rfv %{buildroot}%{python3_sitearch}/PyQt4/uic/port_v2/

%check
diff -u ./sip/QtGui/opengl_types.sip.orig ./sip/QtGui/opengl_types.sip ||:

%files
%doc LICENSE
%{python2_dbus_dir}/qt.so
%dir %{python2_sitearch}/PyQt4/
%{python2_sitearch}/PyQt4/*
%{_qt4_plugindir}/designer/*
%dir %{_qt4_datadir}/qsci/
%dir %{_qt4_datadir}/qsci/api/
%dir %{_qt4_datadir}/qsci/api/python/
%{_qt4_datadir}/qsci/api/python/PyQt4.api

%files devel
%{_bindir}/*
%{_datadir}/sip/PyQt4/

%files help
%doc doc/* examples/ NEWS README

%files -n python3-PyQt4
%{python3_dbus_dir}/qt.so
%dir %{python3_sitearch}/PyQt4/
%{python3_sitearch}/PyQt4/*

%files -n python3-PyQt4-devel
%{_bindir}/*
%dir %{_datadir}/python3-sip/
%{_datadir}/python3-sip/PyQt4/

%changelog
* Fri Feb 14 2020 fengbing <fengbing7@huawei.com> - 4.12.1-12
- Pakcage init
