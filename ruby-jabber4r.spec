Summary:	Jabber library for Ruby
Summary(pl):	Biblioteka Jabber dla jêzyka Ruby
Name:		ruby-jabber4r
Version:	0.6.0
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/376/jabber4r-%{version}.tar.gz
# Source0-md5:	e5e0bc060bd01389714c3598cf379e4d
Source1:	setup.rb
URL:		http://jabber4r.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.263
BuildRequires:	ruby-devel
Requires:	ruby-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jabber library for Ruby.

%description%description -l pl
Biblioteka Jabber dla jêzyka Ruby.

%prep
%setup -q -n jabber4r
cp %{SOURCE1} .

%build
ruby setup.rb config \
	--siterubyver=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc -o rdoc/ --main README README lib/* --title "%{name} %{version}" --inline-source
rdoc --ri -o ri lib/*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{_examplesdir}/%{name}}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/*
%{ruby_rubylibdir}/jabber4r
# Does not merge well with others.
%dir %{ruby_ridir}/Jabber
%{ruby_ridir}/Jabber/*
%{_examplesdir}/%{name}
