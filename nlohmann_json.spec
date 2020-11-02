Name:           nlohmann_json
Version:        %{VERSION}
Release:        %{RELEASE}%{?dist}
Summary:        JSON for Modern C++
Group:          System Environment/Libraries
License:	MIT
URL:            https://github.com/nlohmann/json
Source:         %{name}-%{version}.tar.gz      
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  cmake3

%description
JSON for Modern C++

%package devel
Summary:	%{name} development package
Group:		Development/Libraries

%description devel
Development files for %{name}.

%prep
%setup -n json-%{version}

%build
cmake3 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(-,root,root,-)
%doc LICENSE.MIT README.md 
%{_includedir}/nlohmann/json.hpp
%{_libdir}/cmake/%{name}/*.cmake

%changelog
