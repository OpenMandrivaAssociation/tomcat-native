%define tcnver 1
%define lib_name %mklibname tcnative %{tcnver}

Summary:        Tomcat Native Java library
Name:           tomcat-native
Version:        1.1.24
Release:        2
Epoch:          0
License:        Apache License
Group:          Development/Java
URL:            https://tomcat.apache.org/
Source0:	http://www.apache.org/dist/tomcat/tomcat-connectors/native/%{version}/source/%{name}-%{version}-src.tar.gz
Source1:        http://www.apache.org/dist/tomcat/tomcat-connectors/native/%{version}/source/%{name}-%{version}-src.tar.gz.asc
BuildRequires:  apr-devel >= 0:{version}
BuildRequires:  java-devel >= 0:1.4.2
BuildRequires:  java-rpmbuild
BuildRequires:  openssl-devel

%description
The mission of the Tomcat Native Livrary (TCN) is to provide a
free library of C data structures and routines.  This library
contains additional utility interfaces for Java.

%package -n %{lib_name}
Group:          Development/Java
Summary:        Tomcat Native development kit

%description -n %{lib_name}
The mission of the Tomcat Native Livrary (TCN) is to provide a
free library of C data structures and routines.  This library
contains additional utility interfaces for Java.

%package -n %{lib_name}-devel
Group:          Development/Java
Summary:        Tomcat Native development kit
Provides:       %{_lib}tcnative-devel = %{epoch}:%{version}-%{release}
Requires:       %{lib_name} = %{epoch}:%{version}-%{release}
Requires:       apr-devel

%description -n %{lib_name}-devel
The mission of the Tomcat Native Livrary (TCN) is to provide a
free library of C data structures and routines.  This library
contains additional utility interfaces for Java.

%prep
%setup -q -n %{name}-%{version}-src/jni/native

%build
export JAVA_HOME=%{java_home}
%configure2_5x --with-apr=%{_prefix} \
               --includedir=%{_includedir}/apr-%{tcnver}
%make

%install
%makeinstall

%files -n %{lib_name}
%doc ../../KEYS ../../LICENSE ../../NOTICE BUILDING
%{_libdir}/libtcnative-%{tcnver}.so.*

%files -n %{lib_name}-devel
%{_libdir}/libtcnative-%{tcnver}.so
%{_libdir}/pkgconfig/tcnative-%{tcnver}.pc
