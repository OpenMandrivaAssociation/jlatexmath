Summary:	An implementation of LaTeX math mode wrote in Java
Name:		jlatexmath
Version:	1.0.2
Release:	1
License:	GPLv2+
Group:		Development/Java
URL:		http://forge.scilab.org/index.php/p/jlatexmath/
Source0:	http://forge.scilab.org/index.php/p/jlatexmath/downloads/get/jlatexmath-src-%{version}.zip
BuildRequires:	ant >= 0:1.6
BuildRequires:	fop
BuildRequires:	java-rpmbuild
BuildRequires:	jpackage-utils >= 0:1.6
BuildRequires:	xerces-j2
BuildRequires:	xml-commons-apis
BuildRequires:	xml-commons-jaxp-1.3-apis
BuildRequires:	xmlgraphics-commons
Requires:	jpackage-utils
BuildArch:      noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
JLaTeXMath is an implementation of LaTeX math mode wrote in Java.

%prep
%setup -q

# remove all binary libs
find -type f -name "*.jar" -exec rm -rf {} \;

%build
export CLASSPATH=
export OPT_JAR_LIST=:
%ant minimal fop

%install
rm -rf %{buildroot}

# jars
mkdir -p %{buildroot}%{_javadir}
cp -p dist/jlatexmath{,-fop,-minimal}-%{version}.jar %{buildroot}%{_javadir}
cp -p dist/jlm_*.jar %{buildroot}%{_javadir}
pushd  %{buildroot}%{_javadir} 
    #create symlink
    ln -s %{name}-%{version}.jar %{name}.jar
    ln -s %{name}-fop-%{version}.jar %{name}-fop.jar
    ln -s %{name}-minimal-%{version}.jar %{name}-minimal.jar
popd

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_javadir}/*.jar


%changelog
* Thu Aug 04 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.9.6-1mdv2011.0
+ Revision: 693260
+ rebuild (emptylog)

* Thu Aug 04 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.9.6-1
+ Revision: 693259
- Update to latest upstream release

* Wed Jan 26 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.9.3-1
+ Revision: 632910
- Update to version 0.9.3

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.5-2mdv2011.0
+ Revision: 612449
- the mass rebuild of 2010.1 packages

* Sun Jan 31 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.8.5-1mdv2010.1
+ Revision: 498867
- update to new version 0.8.5

* Sun Dec 20 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5-1mdv2010.1
+ Revision: 480466
- add source and spec files
- Created package structure for jlatexmath.


